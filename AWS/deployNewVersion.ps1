aws s3 cp index.zip s3://terraform-serverless-storage-$aws_region/$app_version/index.zip
terraform apply -var "app_version=$app_version" -var "aws_region=$aws_region"