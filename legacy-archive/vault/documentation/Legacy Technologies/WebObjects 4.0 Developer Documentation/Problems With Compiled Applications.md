---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.a.html
archived_at: '2026-07-15T08:00:25.322372Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Post-Install Guide](About%20This%20Document.md)

[!Table of Contents](About%20This%20Document.md) [!Previous Section](Problems%20With%20Scripted%20Applications.md)

#   Problems With Compiled Applications

Running compiled applications exercises more features of the WebObjects framework and development environment. Before attempting to troubleshoot a problem with running a compiled application, make sure you can run a simple scripted application.

#####  -------------------------------------------------------------------------------------------------------------

##  Problem

A simple compiled application won't run properly.

##  Checklist

1. 

   __Make sure the executable has been built.__

> 
>
> On the HP-UX platform, examples are not installed built. You must build them yourself before you can run them. To compile an example, __cd__
> to the example's project directory and type __make__
> . For example:

> ```
> > cd /Apple/Developer.Examples/WebObjects/ObjectiveC/HelloWorldCompiled> make
> ```

#####  -------------------------------------------------------------------------------------------------------------

##  Problem

The Movies application won't run.

##  Checklist

1. 

   __Make sure the application was correctly installed and compiled.__

> 
>
> The Movies application must be compiled before you can run it. In addition, you must create the Movies database (scripts are provided) and install the database model file that is compatible with your database server as described in "[Setting Up the Sample Databases](Setting%20Up%20the%20Sample%20Databases.md#apple-gmytcnzq)
> ."

> 
>
> Check the Movies directory for an directory named __Movies.woa__
> . This is the WebObjects application wrapper. Check the wrapper for an executable file. If the wrapper or the executable doesn't exist, build the Movies application.

> 
>
> On Solaris and HP-UX, you need to build Movies with the correct client libraries and adaptor. Before you build, add the appropriate adaptor framework to the FRAMEWORKS makefile variable. Then uncomment the following line in the __Makefile.preamble__
> to link the appropriate client libraries:

> ```
> include $(MAKEFILEDIR)/pdo-eoadaptor-linking.make
> ```

> 
>
> If Movies compiles and runs but can't access data about the various movies, it's probably because the application can't communicate with the database server.

#####  -------------------------------------------------------------------------------------------------------------

##  Problem

A WebObjects application won't connect to the database server.

##  Checklist

1. 

   __Check that your database server itself is operating correctly.__

Check that the client libraries for your database server are correctly installed on your machine. If so, you can, for example, use the tools supplied with the database server (isql
for Sybase,
sqlplus
for Oracle, and
dbaccess
for Informix) to test that you can connect to the server and execute simple SQL commands.

2. 

   __Make sure that the database model file is accessible to your application__

> 
>
> The model file should be in the __Resources__
> directory under the application's __.woa__
> directory. Taking the Movies application for example, the directory structure would look like this:

> ```
> 	Movies.woa/
> ```

> ```
> 		Movies (the executable file)
> ```

> ```
> 		Resources/Movies.eomodeld   (the model file)
> ```

[!Table of Contents](About%20This%20Document.md)
