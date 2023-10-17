# AWS OpenTelemetry Collector

## What is OpenTelemetry?

The OpenTelemetry Collector is a standalone process designed to receive, process and export telemetry data.
It removes the need to run, operate and maintain multiple agents/collectors in order to support open-source telemetry data formats (e.g. Jaeger, Prometheus, Zipkin, etc.) sending to multiple open-source or commercial back-ends.

The Collector has two different deployment strategies: either running as an agent alongside a service, or as a remote application.
In general, using both is recommended: the agent would be deployed with your service and run as a sidecar; meanwhile, the remote app would be deployed separately, as its own application running in a container or virtual machine.

Here’s a diagram showing the collector architecture:

![](/img/otel-collector-diagram.png)

- If you want to configure it, you need to know that the configuration contains three main components:

  - **RECEIVERS**: They can be push or pull based and is how data gets into the Collector.
  - **EXPORTERS**: They can be push or pull based and is how you send data to one or more backends/destinations.
  - **PROCESSORS**: They run on the data between being received and being exported. Processors are optional.

## Referencias

- [ ] [opentelemetry.io](https://opentelemetry.io/docs/what-is-opentelemetry/)
- [ ] [aws-otel.github.io](https://aws-otel.github.io/docs/introduction)
- [ ] [open-telemetry/opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib)
