from aws_cdk import core
from aws_cdk import aws_dynamodb as dynamodb

class DailyTaskStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define a DynamoDB table for tasks
        tasks_table = dynamodb.Table(
            self,
            "TasksTable",
            partition_key=dynamodb.Attribute(
                name="task_id",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST  # Use on-demand billing
        )

        # Optionally, add any additional attributes you need for tasks.
        # For example, you might add an attribute for task weights.

        # Output the table name for reference
        output = core.CfnOutput(
            self,
            "TasksTableName",
            value=tasks_table.table_name,
            description="Name of the DynamoDB table for tasks"
        )

