---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.4.html
archived_at: '2026-07-15T08:00:22.167558Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Post-Install Guide](About%20This%20Document.md)

[!Table of Contents](About%20This%20Document.md) [!Previous Section](Solaris%20Post-Installation%20Steps.md)

#   HP-UX Post-Installation Steps

After you've finished installing on HP-UX, perform the following steps:

- 

  [Rebuild the Executable WODefaultApp](#apple-gqztonbz)
- 

  [Change the UID for User nobody](#apple-g43dimrr)
- 

  [Obtain and Install Database Client Libraries](#apple-gizdcnbr)
- 

  [Build the Examples](#apple-gi3tcnzy)

##   Rebuild the Executable WODefaultApp

On HP-UX, the Enterprise Objects Framework cannot automatically load your database's client library and its adaptor, as it can on other platforms. Because of this, you must rebuild the __WODefaultApp__
executable, which is installed with WebObjects and is used to run purely scripted applications. If you don't rebuild this executable, any purely scripted applications you run with __WODefaultApp__
won't be able to access the database.

If you answered "y" to all questions you were asked during installation, the __WODefaultApp__
executable has already been rebuilt by the installation process. If you answered "n" to the question about building __WODefaultApp__
or you have installed new client libraries afterwards, you should rebuild __WODefaultApp__
before testing your installation.

To rebuild __WODefaultApp__
, run the __RebuildWODefaultApp__
script located in __/Developer/Examples/WebObjects/Source/WODefaultApp__
.

> 
>
> Note: Each time you create a new project, you'll need to set it up so that it statically links the database's client library and adaptor. To do so, add the appropriate adaptor framework to the FRAMEWORKS makefile variable definition, and uncomment this line in the __Makefile.preamble__
> .

> ```
> include $(MAKEFILEDIR)/pdo-eoadaptor-linking.make
> ```

##   Change the UID for User nobody

If you're using the Apache web server you'll need to change the UID of the user nobody, which is used to launch CGI processes. By default, the UID is -2, which causes setuid to complain about an invalid argument.

Change the nobody UID and nogroup group ID in __/etc/passwd__
and __/etc/group__
to positive numbers.

##   Obtain and Install Database Client Libraries

To use Enterprise Objects Framework on HP-UX, you must have the appropriate database client libraries.

### Oracle

Phone: (800) 542-1170 or call your local sales representative

Ask for: 8.0 SQLNet V2 TCP/IP Client libraries

The Oracle adaptor on HP-UX requires the Oracle 8.0 or 7.3 Client Library. The makefiles are configured for 7.3 or 8.0 (they default to 7.3); with some modifications of the makefiles, you can also link with 7.2.

### Informix

Phone: (800) 331-1763 or call your local sales representative

Ask for: ESQL/C Version 7.23.UC6

If you get the error "INFORMIXSERVER not in sqlhosts file (25596)" but can connect to your database server using the Informix ilogin program, you may need to run SetNet32 to update the environment variables used by Informix.

The Informix client libraries appear to have redundant sources of server information. They use the sqlhosts file (__$INFORMIXDIR/etc/sqlhosts__) as well as a collection of environment variables managed by the Setnet32 program.

See your Informix documentation for more information on the sqlhosts file and the Setnet32 program.

### Sybase

Phone: (800) 685-8225 or call your local sales representative

Ask for: OpenClient/C Version 11.1

### Linking Against the Adaptor

On HP-UX applications must explicitly link against the adaptor framework and the client libraries. New makefiles look for adaptor frameworks and automatically add in the right linker arguments. Simply add the adaptor framework to your project, and set the requisite environment variable specifying where the client libraries are installed. For Oracle set ORACLE_HOME and optionally ORACLE_REL. (The ORACLE_REL flag controls which set of libraries are used. It uses the Oracle 7.3 static link libraries by default, but you can also specify "8.0-static" or "7.3-dynamic".) For Sybase set SYBASE_HOME. For Informix set INFORMIX_HOME.

##   Build the Examples

The section _[Verifying the Installation](Verifying%20the%20Installation.md#apple-gu3tsnju)_ describes how to verify that your installation is working properly by running the examples, some of which are compiled examples. On HP-UX, you must build the examples before you can test your system. If you want to use the WebObjects examples to test your system, build the examples found in __/Developer/Examples/WebObjects__
.

[!Table of Contents](About%20This%20Document.md) [!Next Section](Using%20Microsoft%20Access.md)
