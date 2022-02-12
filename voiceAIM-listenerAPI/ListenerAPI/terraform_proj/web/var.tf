variable "access_key" {
description = "AWS Access key"
default = "......................."
}

variable "secret_key" {
description = "AWS Secret Key"
default = "........................"
}


variable "region" {
description = "AWS region for hosting our your network"
default = "ap-south-1"
}


variable "aws_ami" {
description = "AWS region for hosting our your network"
default = "ami-02d55cb47e83a99a0"
}


variable "key_name" {
description = "Key name for SSH into EC2"
default = "railway"
}

variable "pub_sub_az" {
description = "Key name for SSH into EC2"
default = "ap-south-1a"
}

variable "pri_sub_az" {
description = "Key name for SSH into EC2"
default = "ap-south-1b"
}
