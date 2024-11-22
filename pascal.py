class TreeNode:
    def __init__(self, content=""):
        self.content = content.strip()
        self.children = []

    def __repr__(self, level=0):
        indent = " " * (level * 4)
        xd=self.content.split(";")
        result=""
        for n in xd:
           n=n.strip()
           result += f"{indent}{n}\n"
        for child in self.children:
            result += child.__repr__(level + 1)
        return result


def parse_pascal_tree(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    tokens = data.split()
    stack = []
    root = TreeNode("root")
    current_node = root
    buffer = ""

    for token in tokens:
        if token.lower() == "begin":
            # Cria um novo nó para "begin"
            if buffer.strip():
                current_node.children.append(TreeNode(buffer))
                buffer = ""
            new_node = TreeNode("begin")
            current_node.children.append(new_node)
            stack.append(current_node)
            current_node = new_node
        elif token.lower() == "end":
            # Finaliza o conteúdo atual e volta ao nível superior
            if buffer.strip():
                current_node.children.append(TreeNode(buffer))
                buffer = ""
            current_node = stack.pop() if stack else current_node
        elif token.lower() == "end.":
            # Finaliza o conteúdo atual e volta ao nível superior
            if buffer.strip():
                current_node.children.append(TreeNode(buffer))
                buffer = ""
            current_node = stack.pop() if stack else current_node
        elif token == ";":
            # Finaliza o buffer para criar um nó no mesmo nível
            if buffer.strip():
                current_node.children.append(TreeNode(buffer))
                buffer = ""
        else:
            buffer += (token + " ")

    return root


def main():
    file_name = input("Enter the name of the Pascal file to load: ")

    try:
        tree = parse_pascal_tree(file_name)
        print("\nParsed Pascal Tree:")
        print(tree)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

