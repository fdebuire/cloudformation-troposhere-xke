from troposphere import (Template, GetAtt)
from troposphere.awslambda import Function, Code
from troposphere.cloudformation import AWSCustomObject

t = Template('CustomResourceXke')
t.set_version()


class CustomResourceXke(AWSCustomObject):
    resource_type = "Custom::CustomResourceXke"
    props = {
        'ServiceToken': (str, True),
        'Var1': (str, True),
        'Var2': (str, True),
    }


lambda_definition = """
    const response = require('cfn-response');
    
    exports.handler = async (event, context) => {
        var physicalResourceId = 'find_a_uniq_id';
        try {
            switch (event.RequestType) {
                case 'Create':
                case 'Update':
                case 'Delete':
                    console.info(event.ResourceProperties.Var1);
                    console.info(event.ResourceProperties.Var2);
                    break;
            }
            
            await response.send(event, context, response.SUCCESS, {}, physicalResourceId);
        } catch (error) {
            console.error(error);
            await response.send(event, context, response.FAILED, {}, physicalResourceId);
        }
    }
"""

function_lambda = t.add_resource(Function(
    "FunctionLambdaXke",
    Code=Code(
        ZipFile=lambda_definition
    ),
    Handler="index.handler",
    Role='xkeLambdaRole',
    Runtime="nodejs8.10",
    Timeout=360
))

t.add_resource(CustomResourceXke(
    "CustomResourceXke",
    ServiceToken=GetAtt(function_lambda, "Arn"),
    Var1='var1',
    Var2='var2'
))

print(t.to_yaml())
