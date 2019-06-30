resource "aws_api_gateway_rest_api" "morse_api" {
  name        = "MorseTF"
  description = "Terraform Serverless Morse API"
}

output "base_url" {
  value = "${aws_api_gateway_deployment.morseTF.invoke_url}"
}