from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.boto import BotoInstrumentor
import boto3

# Inicializar OpenTelemetry
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(OTLPSpanExporter()))

# Instrumentar boto3 para enviar trazas
BotoInstrumentor().instrument()

import boto3

def list_resources(aws_profile):
    # Establecer el perfil de AWS
    boto3.setup_default_session(profile_name=aws_profile)

    # Listar buckets S3
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()
    print("Buckets S3:")
    for bucket in buckets['Buckets']:
        print(f"- {bucket['Name']}")

    # Listar instancias EC2
    ec2 = boto3.client('ec2')
    reservations = ec2.describe_instances()
    print("\nInstancias EC2:")
    for reservation in reservations['Reservations']:
        for instance in reservation['Instances']:
            print(f"- ID: {instance['InstanceId']}  Estado: {instance['State']['Name']}  Tipo: {instance['InstanceType']}")

if __name__ == "__main__":
    profile = 'jhoseph'  # Reemplaza 'tu_profile_aqui' con el nombre de tu profile
    list_resources(profile)