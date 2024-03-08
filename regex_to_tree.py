from regex.nodes.LeafRegexNode import LeafRegexNode
from regex.nodes.BinaryRegexNode import BinaryRegexNode, BinaryOperationType
from regex.nodes.UnaryRegexNode import UnaryRegexNode

# Example of correct regexpr: (a*b*(a+c))*+b
# Do not use spaces between symbols

def build_tree(text: str):
    if len(text) == 1:
        return LeafRegexNode(text)
    
    elif text[0] == '(':
        balance = 1
        pos = 0
        while balance != 0:
            pos += 1
            if text[pos] == '(':
                balance += 1
            elif text[pos] == ')':
                balance -= 1
        tree_1 = build_tree(text[1:pos])
        if pos < len(text) - 1 and text[pos + 1] == '*':
            tree_1 = UnaryRegexNode(tree_1)
            pos += 1
        
        if pos < len(text) - 1:
            if text[pos + 1] == '+':
                tree_2 = build_tree(text[pos + 2:])
                return BinaryRegexNode(tree_1, tree_2, BinaryOperationType.UNITE)
            else:
                tree_2 = build_tree(text[pos + 1:])
                return BinaryRegexNode(tree_1, tree_2, BinaryOperationType.CONCATENATION)
        
        else:
            return tree_1
        
    
    else:
        pos_plus = 0
        pos_br = 0

        while pos_plus < len(text) and text[pos_plus] != '+':
            pos_plus += 1
        
        while pos_br < len(text) and text[pos_br] != '(':
            pos_br += 1

        if pos_br < pos_plus:
            return BinaryRegexNode(build_tree(text[0:pos_br]), build_tree(text[pos_br:]), BinaryOperationType.CONCATENATION)
        else:
            if pos_plus == len(text):
                tree_1 = build_tree(text[0])
                if text[1] == '*':
                    tree_1 = UnaryRegexNode(tree_1)
                    if len(text) > 2:
                        return BinaryRegexNode(tree_1, build_tree(text[2:]), BinaryOperationType.CONCATENATION)
                    else: 
                        return tree_1
                    
                else:
                    return BinaryRegexNode(tree_1, build_tree(text[1:]), BinaryOperationType.CONCATENATION)
                
            else:
                return BinaryRegexNode(build_tree(text[:pos_plus]), build_tree(text[pos_plus + 1:]), BinaryOperationType.UNITE)
            
            

        
            
