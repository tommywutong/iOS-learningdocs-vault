---
title: WebObjects Deployment Guide Using JavaMonitor
apple_id: TP30001009
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Deployment/Deploying_Applications/Introduction/Introduction.html
archived_at: '2026-07-18T02:15:56.185233Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](WebObjects%20Deployment.md)

# Introduction to WebObjects Deployment Guide Using JavaMonitor

This document describes the tools and techniques that system administrators and website managers perform to deploy WebObjects applications. The WebObjects Deployment package allows you to deploy applications developed with the WebObjects Development package, so that they can be accessed through a Web server. You need a WebObjects deployment license to deploy WebObjects applications.

This document is intended primarily for system administrators. Application developers can also benefit from the information it provides but it’s not required reading for them.

This document assumes you have a solid background in system administration. You must be familiar with the operation of your platform, especially how to use its command shell editor to issue commands. You must also be acquainted with the operation of your Web server software and TCP/IP networking. Knowledge of WebObjects application development is helpful, but not required.

To deploy WebObjects applications and to administer a deployment, you need to become acquainted with the deployment model of WebObjects. This document shows you how your Web server interacts with the elements of a WebObjects deployment. It also explains what measures you should take to increase your site’s performance.

WebObjects Deployment provides tools for most of the tasks you need to accomplish on a regular basis to maintain your site. If you prefer doing things manually, you can use the command line to start individual application instances or the deployment tools themselves.

This document has the following chapters:

- [WebObjects Deployment](WebObjects%20Deployment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrqfvkfawcsivddcmbr) gives you an overview of the deployment approach taken with WebObjects 5. In addition, it lists the ways in which WebObjects Deployment helps you to maintain a secure site.
- [Installing Software](Installing%20Software.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrrfvkfawcsivddcmbr) explains which WebObjects Deployment components need to be installed on a computer, taking into account the computer’s purpose in your site. It also shows you how to build HTTP adaptors, which are interfaces between applications and web servers.
- [HTTP Adaptors](HTTP%20Adaptors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrsfvkfawcsivddcmbr) describes the function of the HTTP adaptor in your site. It also describes how you customize the adaptors included in WebObjects Deployment if the default configuration does not suit your needs. State discovery is how the HTTP adaptor keeps track of the application instances of your site. The chapter describes the different ways that the adaptor can obtain that information and how you configure the adaptor to use one of those methods.
- [Managing Application Instances](Managing%20Application%20Instances.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrtfvbecssfijbukri) introduces you to the deployment tools you use to configure and maintain your site. It also describes the mechanism used in WebObjects to ensure that application instances are always running, helping you maximize your site’s up time.
- [Deployment Tasks](Deployment%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrufvkfawcsivddcmbr) explains how to perform configuration and maintenance tasks on your site. It also shows how to maintain multiple sites using the same hardware.
- [Application Administration](Application%20Administration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrvfvkfawcsivddcmbr) shows you how to monitor and improve your site’s performance.
- [Application URLs](Application%20URLs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambzfvbuqmrrguwvgvzu) describes the format of WebObjects application URLs so that you can use a web browser to connect directly to a running WebObjects application.
- [JMX Monitoring](JMX%20Monitoring.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambzfvbuqmrrgywvgvzr) describes how to use JMX to monitor WebObjects applications.
- [Deployment Issues with Java Client](Deployment%20Issues%20with%20Java%20Client.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydanrxfvkfawcsivddcmbr) lists issues to keep in mind when deploying Java Client applications. It also tells you what to do if you want to deploy WebObjects 4.5.1 applications together with WebObjects 5.x applications.

To get an overview of the WebObjects platform, you should read _[WebObjects Overview](../WebObjects%20Overview/Introduction%20to%20WebObjects%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamby)_. You can find general information about WebObjects at [http://developer.apple.com/webobjects](https://developer.apple.com/webobjects).

Read _[WebObjects Application Properties Reference](../WebObjects%20Application%20Properties%20Reference/Introduction%20to%20WebObjects%20Application%20Properties%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamrq)_ for a complete list of all the application properties for WebObjects applications, JavaMonitor, and wotaskd. These application properties correspond to command-line arguments that you can use to configure your WebObjects applications and tools for the particular deployment environment. Most of options in the JavaMonitor user interface correspond to JavaMonitor properties described in _[WebObjects Application Properties Reference](../WebObjects%20Application%20Properties%20Reference/Introduction%20to%20WebObjects%20Application%20Properties%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamrq)_.

[Next](WebObjects%20Deployment.md)

