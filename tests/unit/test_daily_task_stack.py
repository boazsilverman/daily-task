import aws_cdk as core
import aws_cdk.assertions as assertions

from daily_task.daily_task_stack import DailyTaskStack

# example tests. To run these tests, uncomment this file along with the example
# resource in daily_task/daily_task_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DailyTaskStack(app, "daily-task")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
