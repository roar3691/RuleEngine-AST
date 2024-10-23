import re

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left
        self.right = right
        self.value = value

class ImprovedRuleEngine:
    def __init__(self):
        self.rules = []

    def create_rule(self, rule_string):
        node = Node('rule', value=rule_string)
        self.rules.append(node)
        return node

    def combine_rules(self, rules):
        if not rules:
            return None
        combined = Node('operator', value='AND')  # Default to AND for combination
        for rule in rules:
            if combined.left is None:
                combined.left = self.create_rule(rule)
            else:
                combined.right = self.create_rule(rule)
        return combined

    def evaluate_rule(self, ast, data):
        if ast is None:
            print("Error: The AST is None.")
            return False
        if ast.type == 'rule':
            return self.safe_eval(ast.value, data)
        elif ast.type == 'operator':
            left_value = self.evaluate_rule(ast.left, data)
            right_value = self.evaluate_rule(ast.right, data)
            if ast.value == 'AND':
                return left_value and right_value
            elif ast.value == 'OR':
                return left_value or right_value
        return False

    def safe_eval(self, rule_string, data):
        print(f'Initial Rule String: {rule_string}')  # Debugging statement
        print(f'Initial Data: {data}')  # Debugging statement
        for key, value in data.items():
            rule_string = rule_string.replace(key, str(value))

        print(f'Modified Rule String: {rule_string}')  # Debugging statement

        pattern = r'\s*(\w+)\s*([<>=!]+)\s*([^\s)]+)'
        matches = re.findall(pattern, rule_string)
        for match in matches:
            left, operator, right = match
            left_value = data.get(left)

            if left_value is None:
                print(f"Warning: '{left}' not found in data.")
                return False

            right_value = float(right) if right.replace('.', '', 1).isdigit() else right.strip('"')

            if operator == '>':
                if not (left_value > right_value):
                    return False
            elif operator == '<':
                if not (left_value < right_value):
                    return False
            elif operator == '==':
                if not (left_value == right_value):
                    return False
        return True

    def modify_rule(self, existing_rule_str, new_rule_string):
        for idx, rule in enumerate(self.rules):
            if rule.value == existing_rule_str:
                self.rules[idx].value = new_rule_string
                return True  # Modification successful
        return False  # Rule not found

# Example Usage to demonstrate functionality
if __name__ == "__main__":
    engine = ImprovedRuleEngine()
    engine.create_rule("(age > 30 AND department == 'Sales')")
    engine.modify_rule("(age > 30 AND department == 'Sales')", "(age > 25 AND department == 'Marketing')")
    combined_rule = engine.combine_rules([rule.value for rule in engine.rules])
    sample_data = {'age': 35, 'department': 'Marketing'}
    evaluation_result = engine.evaluate_rule(combined_rule, sample_data)
    print(f'Final Evaluation Result: {evaluation_result}')