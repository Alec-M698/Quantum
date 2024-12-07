import sys
import os
import re

def run_quantum_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    with open(file_path, 'r') as file:
        code = file.read()
        class SimpleLang:
            def __init__(self):
                self.variables = {}
                self.constants = {}
                self.functions = {}

            def read_file(self, file_path):
                with open(file_path, 'r') as file:
                    return file.read()

            def write_file(self, file_path, content):
                with open(file_path, 'w') as file:
                    file.write(content)

            def parse_line(self, line):
                
                # Handle constant declaration
                const_match = re.match(r'const (\w+) = (.+)', line)
                if const_match:
                    const_name = const_match.group(1)
                    const_value = eval(const_match.group(2), {"read_file": self.read_file, "write_file": self.write_file, "int": int, "str": str, "list": list, "dict": dict}, self.variables)
                    if const_name in self.variables:
                        raise ValueError(f"Cannot declare constant {const_name} as it is already a variable")
                    self.constants[const_name] = const_value
                    return

                # Handle variable declaration
                var_match = re.match(r'var (\w+) = (.+)', line)
                if var_match:
                    var_name = var_match.group(1)
                    var_value = eval(var_match.group(2), {"read_file": self.read_file, "write_file": self.write_file, "int": int, "str": str, "list": list, "dict": dict}, self.variables)
                    self.variables[var_name] = var_value
                    return

                # Handle variable reassignment
                var_reassign_match = re.match(r'(\w+) = (.+)', line)
                if var_reassign_match:
                    var_name = var_reassign_match.group(1)
                    var_value = eval(var_reassign_match.group(2), {"read_file": self.read_file, "write_file": self.write_file, "int": int, "str": str, "list": list, "dict": dict}, self.variables)
                    if var_name in self.constants:
                        raise ValueError(f"Cannot reassign constant {var_name}")
                    self.variables[var_name] = var_value
                    return


                # Handle print statement
                print_match = re.match(r'print\((.+)\)', line)
                if print_match:
                    to_print = eval(print_match.group(1), {"read_file": self.read_file, "write_file": self.write_file, "int": int, "str": str, "list": list, "dict": dict}, {**self.variables, **self.constants})
                    if isinstance(to_print, tuple):
                        print(" ".join(map(str, to_print)))
                    else:
                        print(to_print)
                    return

                # Handle input statement
                input_match = re.match(r'var (\w+) = input\("(.+)"\)', line)
                if input_match:
                    var_name = input_match.group(1)
                    prompt = input_match.group(2)
                    user_input = input(prompt + " ")
                    self.variables[var_name] = user_input
                    return

                # Handle file read
                file_read_match = re.match(r'var (\w+) = read_file\("(.+)"\)', line)
                if file_read_match:
                    var_name = file_read_match.group(1)
                    file_path = file_read_match.group(2)
                    self.variables[var_name] = self.read_file(file_path)
                    return

                # Handle file write
                file_write_match = re.match(r'write_file\("(.+)", (.+)\)', line)
                if file_write_match:
                    file_path = file_write_match.group(1)
                    content = eval(file_write_match.group(2), {"read_file": self.read_file, "write_file": self.write_file, "int": int, "str": str, "list": list, "dict": dict}, self.variables)
                    self.write_file(file_path, content)
                    return

                # Handle if statement
                if_match = re.match(r'if (.+):', line)
                if if_match:
                    condition = eval(if_match.group(1), {"read_file": self.read_file, "write_file": self.write_file, "int": int, "str": str, "list": list, "dict": dict}, self.variables)
                    return 'if', condition

                # Handle elif statement
                elif_match = re.match(r'elif (.+):', line)
                if elif_match:
                    condition = eval(elif_match.group(1), {"read_file": self.read_file, "write_file": self.write_file, "int": int, "str": str, "list": list, "dict": dict}, self.variables)
                    return 'elif', condition

                # Handle else statement
                if line == 'else:':
                    return 'else'

                # Handle end of if block
                if line == 'endif':
                    return 'endif'

                # Handle function declaration
                func_match = re.match(r'func (\w+)\(\)', line)
                if func_match:
                    func_name = func_match.group(1)
                    self.functions[func_name] = []
                    return func_name

                # Handle end of function declaration
                if line == 'endfunc':
                    return 'endfunc'

                # Handle function call
                func_call_match = re.match(r'(\w+)\(\)', line)
                if func_call_match:
                    func_name = func_call_match.group(1)
                    if func_name in self.functions:
                        for func_line in self.functions[func_name]:
                            self.parse_line(func_line)
                    else:
                        raise NameError(f"Function {func_name} not defined")
                    return

                # Handle for loop
                for_match = re.match(r'for (\w+) in range\((\d+), (\d+)\):', line)
                if for_match:
                    var_name = for_match.group(1)
                    start = int(for_match.group(2))
                    end = int(for_match.group(3))
                    return 'for', var_name, start, end

                # Handle end of for loop
                if line == 'endfor':
                    return 'endfor'

                # Handle while loop
                while_match = re.match(r'while (.+):', line)
                if while_match:
                    condition = while_match.group(1)
                    return 'while', condition

                # Handle end of while loop
                if line == 'endwhile':
                    return 'endwhile'

                # Handle switch statement
                switch_match = re.match(r'switch (.+):', line)
                if switch_match:
                    var_name = switch_match.group(1)
                    return 'switch', var_name

                # Handle case statement
                case_match = re.match(r'case (.+):', line)
                if case_match:
                    case_value = case_match.group(1)
                    return 'case', case_value

                # Handle end of switch statement
                if line == 'endswitch':
                    return 'endswitch'

                # Handle multi-line comments
                if line.startswith('/*'):
                    return 'multiline_comment_start'

                if line.endswith('*/'):
                    return 'multiline_comment_end'

                # Handle comments
                if line.startswith('#'):
                    return
                
                raise SyntaxError(f"Unknown command: {line}")

            def run(self, code):
                current_func = None
                in_if_block = False
                execute_if_block = False
                in_for_loop = False
                for_loop_var = None
                for_loop_start = 0
                for_loop_end = 0
                in_while_loop = False
                while_condition = None
                in_switch = False
                switch_var = None
                case_matched = False
                in_multiline_comment = False
                while_loop_lines = []
                for line in code.split('\n'):
                    line = line.strip()
                    if line:
                        if in_multiline_comment:
                            if line.endswith('*/'):
                                in_multiline_comment = False
                        elif line.startswith('/*'):
                            in_multiline_comment = True
                        elif current_func:
                            if line == 'endfunc':
                                current_func = None
                            else:
                                self.functions[current_func].append(line)
                        elif in_if_block:
                            if line == 'endif':
                                in_if_block = False
                            elif line.startswith('elif ') or line == 'else:':
                                if not execute_if_block:
                                    result = self.parse_line(line)
                                    if result[0] == 'elif':
                                        execute_if_block = result[1]
                                    elif result[0] == 'else':
                                        execute_if_block = True
                            elif execute_if_block:
                                self.parse_line(line)
                        elif in_for_loop:
                            if line == 'endfor':
                                in_for_loop = False
                            else:
                                for i in range(for_loop_start, for_loop_end):
                                    self.variables[for_loop_var] = i
                                    self.parse_line(line)
                        elif in_while_loop:
                            if line == 'endwhile':
                                in_while_loop = False
                                while eval(while_condition, {}, self.variables):
                                    for while_line in while_loop_lines:
                                        self.parse_line(while_line)
                                while_loop_lines = []
                            else:
                                while_loop_lines.append(line)
                        elif in_switch:
                            if line == 'endswitch':
                                in_switch = False
                            elif line.startswith('case '):
                                case_value = self.parse_line(line)[1]
                                if self.variables[switch_var] == eval(case_value, {}, self.variables):
                                    case_matched = True
                                else:
                                    case_matched = False
                            elif case_matched:
                                self.parse_line(line)
                        else:
                            result = self.parse_line(line)
                            if result and result != 'endfunc':
                                if result[0] == 'if':
                                    in_if_block = True
                                    execute_if_block = result[1]
                                elif result[0] == 'for':
                                    in_for_loop = True
                                    for_loop_var = result[1]
                                    for_loop_start = result[2]
                                    for_loop_end = result[3]
                                elif result[0] == 'while':
                                    in_while_loop = True
                
                                    while_condition = result[1]
                                elif result[0] == 'switch':
                                    in_switch = True
                                    switch_var = result[1]
                                elif result[0] == 'multiline_comment_start':
                                    in_multiline_comment = True
                                else:
                                    current_func = result
        print(f"Running Quantum code from '{file_path}'")
        interpreter = SimpleLang()
        interpreter.run(code)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quantum.py <path_to_quantum_file>")
    else:
        file_path = sys.argv[1]
        run_quantum_file(file_path)
