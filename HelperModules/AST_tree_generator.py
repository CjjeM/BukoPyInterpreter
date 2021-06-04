class AST:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return node.tok.value

    def visit_StringNode(self, node):
        return node.tok.value

    def visit_VarAccessNode(self, node):
        var_name = node.var_name_tok.value
        return (type(node).__name__ + f"(Identifier={var_name})").replace("\\", "")

    def visit_VarAssignNode(self, node):
        var_name = node.var_name_tok.value
        value = self.visit(node.value_node)
        return (type(node).__name__ + f"(Identifier={var_name}, Value={value})").replace("\\", "")

    def visit_BinOpNode(self, node):
        left = self.visit(node.left_node)
        optok = node.op_tok
        right = self.visit(node.right_node)
        return (type(node).__name__+f"(Left={left} op={optok} Right={right})").replace("\\", "")

    def visit_UnaryOpNode(self, node):
        if node.op_tok.type == 'MINUS':
            op = "USub"
        else:
            op = "Not"

        return (type(node).__name__ + f"(Num={node.node}, Operator={op})").replace("\\", "")

    def visit_ListNode(self, node):
        element_nodes = [self.visit(node) for node in node.element_nodes]
        return (type(node).__name__ + f"(Body={element_nodes})").replace("\\", "")

    def visit_IfNode(self, node):
        ifNode = [f"IfBody[Condition={self.visit(condition)} Body={self.visit(expr)}]" for condition, expr, should_return_null in node.cases]
        elseNode = node.else_case

        if elseNode is not None:
            return (type(node).__name__ + f"(If={ifNode} Else={self.visit(elseNode[0])})").replace("\\", "")
        return (type(node).__name__ + f"(If={ifNode})").replace("\\", "")

    def visit_ForNode(self, node):
        start = self.visit(node.start_value_node)
        end = self.visit(node.end_value_node)
        step = node.step_value_node
        body = self.visit(node.body_node)
        return (type(node).__name__ + f"(Start={start} End={end} Step={step} Body={body})").replace("\\", "")

    def visit_WhileNode(self, node):
        condition = self.visit(node.condition_node)
        body = self.visit(node.body_node)
        return (type(node).__name__ + f"(Condition={condition} Body={body})").replace("\\", "")

    def visit_CallNode(self, node):
        node_to_call = node.node_to_call
        arg_nodes = node.arg_nodes

        if len(arg_nodes) != 0:
            return f"Call(Name={self.visit(node_to_call)} Args='{self.visit(arg_nodes[0])}')"
        return f"Call(Name={self.visit(node_to_call)} Args={None})"

    def print_ast(self, ast):
        list_node = ast.node
        elements = list_node.element_nodes

        for element in elements:
            method_name = f'visit_{type(element).__name__}'
            method = getattr(self, method_name)
            print(method(element))
            print()

        print("\n")
