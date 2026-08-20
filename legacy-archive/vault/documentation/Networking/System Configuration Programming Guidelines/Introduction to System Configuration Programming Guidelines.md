---
title: System Configuration Programming Guidelines
apple_id: TP40001065
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: SystemConfiguration
published: '2006-02-07'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/SystemConfigFrameworks/SC_Intro/SC_Intro.html
archived_at: '2026-07-15T08:18:25.514692Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](System%20Configuration%20Goals%20and%20Architecture.md)

# Introduction to System Configuration Programming Guidelines

This document describes the architecture of the system configuration services in OS X and the APIs in the System Configuration framework. It describes how users and applications use the configurable network preferences and how applications can use the framework APIs to accomplish various tasks.

The System Configuration framework provides powerful, flexible support for establishing and maintaining access to configurable network and system resources. It offers your application the ability to determine, set, and maintain configuration settings and to detect and respond dynamically to changes in that information.

The framework supports a wide range of configuration management, including high-level access to network services. Although the bulk of the System Configuration APIs were available in OS X version 10.1, later versions of OS X have included some changes and additions. This document focuses on the System Configuration APIs available in OS X version 10.3.

The audience for this document comprises two main groups:

- Developers of network configuration or dialer software.
- Developers of applications that need to request and use network connections.

If you are developing an application that defines network services, initiates IP networking or creates a PPP connection, you should concentrate on the network preferences and configuration APIs. If you’re developing an application that needs to know if a remote host is reachable or initiate a PPP connection, you should focus on the reachability and connection APIs.

This document is divided into four chapters:

- [System Configuration Goals and Architecture](System%20Configuration%20Goals%20and%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgiwugsceireecqsj) describes the System Configuration framework in its entirety, paying special attention to the interaction of the network preferences, configuration agents, and APIs.
- [Components of the System Configuration Framework](Components%20of%20the%20System%20Configuration%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqg4wugsceireecqsj) describes the individual System Configuration framework components in greater detail. In this chapter, you learn about how the components work together and how the configuration agents do their work.
- [The System Configuration Schema](The%20System%20Configuration%20Schema.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgmwugscejfeeiq2h) describes the structure of network preferences and introduces the System Configuration schema that defines it. This chapter also describes how the configuration agents use the schema’s keys and values and when you might need to use them.
- [Determining Reachability and Getting Connected](Determining%20Reachability%20and%20Getting%20Connected.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgqwuescbizbecscj) introduces the reachability and connectivity APIs and describes how applications can use them.

The chapters you read depend on the goals of your application. All developers new to the System Configuration framework should read [System Configuration Goals and Architecture](System%20Configuration%20Goals%20and%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgiwugsceireecqsj). Then, if you’re developing an ISP or dialer application that needs to manipulate network configurations, you should read [Components of the System Configuration Framework](Components%20of%20the%20System%20Configuration%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqg4wugsceireecqsj) and [The System Configuration Schema](The%20System%20Configuration%20Schema.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgmwugscejfeeiq2h). If, on the other hand, you’re developing an application that initiates PPP connections or determines if a remote host is reachable, you can skip to the last chapter, [Determining Reachability and Getting Connected](Determining%20Reachability%20and%20Getting%20Connected.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrvfvbuqmrqgqwuescbizbecscj).

Apple provides comprehensive API reference documentation of the System Configuration framework. On the web, see _[System Configuration Framework Reference](https://developer.apple.com/documentation/systemconfiguration)_.

In addition, Apple provides several code samples that illustrate various network configuration and connection tasks. These samples are available on the web at [http://developer.apple.com/samplecode/Sample_Code/Networking.htm](https://developer.apple.com/samplecode/Sample_Code/Networking.htm).

When you install the Developer Package, you get developer documentation as well as tools and sample code. The System Configuration API reference documentation is available at `/Developer/ADC Reference Library/documentation/Networking/Reference`.

[Next](System%20Configuration%20Goals%20and%20Architecture.md)

