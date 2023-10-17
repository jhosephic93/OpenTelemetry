# Otel AWS Lambda Auto-Instrumentation | Python3.11

## Getting started

1. Create AWS Lambda

    ![](../img/1.jpg)

2. Create with config.
    - **Author from scratch**
    - **Function name:** LambdaFunctionPython3-AKS
    - **Runtime:** Python 3.11

3. Add Layer on Lambda.
    - In the tab **code** on section **Layers**
    - Click on Add a layer.

    ![](../img/2.jpg)

    - Select **Specify an ARN**, enter the arn from Python 3.11. See See [Reference Link](#referencias).

    ![](../img/3.jpg)

4. Add **Environment variables**
    - In the tab **Configuration** on section **Environment variables**
    - Click on **Edit**.

    | Key                                            | Value                        |
    | ---------------------------------------------- | ---------------------------- |
    | AWS_LAMBDA_EXEC_WRAPPER                        | /opt/otel-instrument         |
    | OTEL_EXPORTER_OTLP_ENDPOINT                    | <http://20.96.246.125:4318>    |
    | OTEL_EXPORTER_OTLP_PROTOCOL                    | http/protobuf                |

5. Add **Traces** | OPTIONAL
    - In the tab **Configuration** on section **Monitoring and operations tools**
    - Click on **Edit**.
    - Enable **Active tracing**

6. Validation.
    - In the tab **Test**
    - Click on **Test**

    ![](../img/4.jpg)

<a id="referencias"></a>

## Referencias

- [ ] [Find the most recent instrumentation layer release](https://github.com/open-telemetry/opentelemetry-lambda/releases)
