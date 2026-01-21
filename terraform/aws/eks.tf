provider "aws" {
  region = "us-east-1"
}

resource "aws_iam_role" "eks_role" {
  name = "eks-dr-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "eks.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_eks_cluster" "eks" {
  name     = "eks-dr"
  role_arn = aws_iam_role.eks_role.arn

  vpc_config {
    subnet_ids = ["subnet-xxxxxx"]
  }
}

