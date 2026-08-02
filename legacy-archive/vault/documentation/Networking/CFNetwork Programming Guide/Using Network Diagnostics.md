---
title: CFNetwork Programming Guide
apple_id: TP30001132
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: CFNetwork
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/UsingNetworkDiagnostics/UsingNetworkDiagnostics.html
archived_at: '2026-07-15T08:18:13.025601Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CFNetwork Programming Guide](Introduction%20to%20CFNetwork%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Working%20with%20FTP%20Servers.md)

# Using Network Diagnostics

In many network-based applications, network-based errors may occur that are unrelated to your application. However, most users are probably unaware of why an application is failing. The CFNetDiagnostics API allows you a quick and easy way to help the user fix their network problems with little work on your end.

If your application is using a CFStream object, then create a network diagnostic reference (`CFNetDiagnosticRef`) by calling the function `CFNetDiagnosticCreateWithStreams`. `CFNetDiagnosticCreateWithStreams` takes an allocator, a read stream, and a write stream as arguments. If your application uses only a read stream or a write stream, the unused argument should be set to `NULL`.

You can also create a network diagnostic reference straight from a URL if no stream exists. To do this, call the `CFNetDiagnosticCreateWithURL` function and pass it an allocator, and the URL as a `CFURLRef`. It will return a network diagnostic reference for you to use.

To diagnose the problem through the Network Diagnostic Assistant, call the `CFNetDiagnosticDiagnoseProblemInteractively` function and pass the network diagnostic reference. Listing 6-1 shows how to use CFNetDiagnostics with streams implemented on a run loop.

__Listing 6-1__  Using the CFNetDiagnostics API when a stream error occurs

```
    case kCFStreamEventErrorOccurred:
        CFNetDiagnosticRef diagRef =
            CFNetDiagnosticCreateWithStreams(NULL, stream, NULL);
        (void)CFNetDiagnosticDiagnoseProblemInteractively(diagRef);
        CFStreamError error = CFReadStreamGetError(stream);
        reportError(error);
        CFReadStreamClose(stream);
        CFRelease(stream);
        break;
```

CFNetworkDiagnostics also gives you the ability to retrieve the status of the problem rather than using the Network Diagnostic Assistant. This is accomplished by calling `CFNetDiagnosticCopyNetworkStatusPassively`, which returns a constant value such as `kCFNetDiagnosticConnectionUp` or `kCFNetDiagnosticConnectionIndeterminate`.

[Next](Document%20Revision%20History.md)[Previous](Working%20with%20FTP%20Servers.md)

