# -*- coding: utf-8 -*-


def aa(inorder, postorder):
    if not postorder: return
 
    # 后序遍历的最后一个节点就是当前的中间点
    root_val = postorder[-1]
    root = TreeNode(root_val)
 
    # 获取切割点，切割中序数组得到中序数组左右部分
    idx = inorder.index(root_val)
    in_left = inorder[:idx]
    in_right = inorder[idx+1:]
    
    # 切割后序数组，得到后序数组左右部分, PS: 中序数组大小要跟后序数组大小相同
    po_left = postorder[:len(in_left)]
    po_right = postorder[len(in_left):len(postorder)-1]   

    # 递归
    root.left = aa(in_left, po_left)
    root.right = aa(in_right, po_right)
    return root
