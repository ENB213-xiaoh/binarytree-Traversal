package com.company;

import java.util.LinkedList;
import java.util.Stack;

public class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;

    public TreeNode(int value) {
        this.value = value;
    }

    public TreeNode(int value, TreeNode left, TreeNode right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    public void preOrderTraversalRecursion(TreeNode root) {
        if (root == null) return;
        System.out.print(root.value + " ");
        preOrderTraversalRecursion(root.left);
        preOrderTraversalRecursion(root.right);
    }

    public void preOrderTraversalIteration(TreeNode root) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode tmpNode = root;
        while (tmpNode != null || !stack.isEmpty()) {
            if (tmpNode != null) {
                System.out.print(tmpNode.value + " ");
                stack.push(tmpNode);
                tmpNode = tmpNode.left;
            }
            else {
                TreeNode node = stack.pop();
                tmpNode = node.right;
            }
        }
    }

    public void inOrderTraversalRecursion(TreeNode root) {
        if (root == null) return;
        inOrderTraversalRecursion(root.left);
        System.out.print(root.value + " ");
        inOrderTraversalRecursion(root.right);
    }

    public void inOrderTraversalIteration(TreeNode root) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        TreeNode tmpNode = root;
        while (tmpNode != null || !stack.isEmpty()) {
            if (tmpNode != null) {
                stack.push(tmpNode);
                tmpNode = tmpNode.left;
            }
            else {
                TreeNode node = stack.pop();
                System.out.print(node.value + " ");
                tmpNode = node.right;
            }
        }
    }

    public void postOrderTraversalRecursion(TreeNode root) {
        if (root == null) return;
        postOrderTraversalRecursion(root.left);
        postOrderTraversalRecursion(root.right);
        System.out.print(root.value + " ");
    }

    public void postOrderTraversalIteration(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        while (true) {
            while (root != null) {
                stack.push(root);
                stack.push(root);
                root = root.left;
            }
            if (stack.isEmpty()) return;
            root = stack.pop();

            if (!stack.isEmpty() && stack.peek() == root)
                root = root.right;
            else {
                System.out.print(root.value + " ");
                root = null;
            }
        }
    }
}
