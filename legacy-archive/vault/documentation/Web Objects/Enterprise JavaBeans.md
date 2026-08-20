---
title: Enterprise JavaBeans
apple_id: TP30001012
resource_type: Guide
platform: Java
topic: Cross Platform
technology: null
published: '2004-10-05'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_JavaBeans/AboutThisBook/AboutThisBook.html
archived_at: '2026-07-18T02:20:56.452067Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_JavaBeans/Introduction/Introduction.html)

# About This Document

Enterprise JavaBeans (EJB) is a specification that provides an infrastructure through which solution providers can develop components that you can purchase and use in your WebObjects applications with minimal effort. In addition, the components can be configured to work with a variety of databases (as long as the database supports JDBC). The key ingredient in these components is enterprise beans. Enterprise beans are business objects that contain logic used to perform specific tasks. They are similar to enterprise objects in WebObjects, but can be used in application servers from multiple vendors.

Enterprise JavaBeans is part of Sun’s Java 2 Platform, Enterprise Edition (J2EE) strategy. J2EE provides an abstraction from the implementation details of databases, directory services, communication protocols, and so on. EJB aims at providing you an abstraction layer between your application’s business logic and the implementation-specific details of the data entities it uses. An enterprise-bean developer doesn’t have to worry about which database is used when the bean is deployed, freeing her to concentrate on the business problem. WebObjects implements version 1.1 of the EJB specification.

Enterprise JavaBeans support in WebObjects lets you integrate third-party, enterprise-bean–based solutions in your WebObjects applications. This means you can purchase components that solve a particular problem, so that you can focus on issues specific to your business. In addition, you can develop your own enterprise beans using WebObjects tools. You must keep in mind, however, that Enterprise Object technology does not complement, nor can be efficiently combined with Enterprise JavaBeans. When you write enterprise beans, you use a persistence-management system that is completely separate from Enterprise Objects. You should not have enterprise beans that use the same database tables that enterprise-object classes are mapped to.

You should read this document if you want to learn how to incorporate an EJB-based solution in a WebObjects application or you want to develop your own enterprise beans using WebObjects tools. However, it is not the purpose of this document to teach you EJB development. If you want to develop enterprise beans, you must already have a sound knowledge of the technology.

The document includes the following chapters:

- [Introduction to Enterprise JavaBeans](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_JavaBeans/Introduction/Introduction.html#//apple_ref/doc/uid/TP30000098-CJBCFFAG) provides an overview of Enterprise JavaBeans technology and how it’s implemented in WebObjects.
- [Developing Session Beans](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_JavaBeans/SimpleSessionBean/SimpleSessionBean.html#//apple_ref/doc/uid/TP30000099-BBCBJDAG) walks you through the development of a simple session bean and its use in a client application.
- [Developing Bean Frameworks](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_JavaBeans/FrameworkDevelopment/FrameworkDevelopment.html#//apple_ref/doc/uid/TP30000101-BBCGBBEF) lists the steps you take to create and maintain bean frameworks.
- [Configuring Applications](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_JavaBeans/ContainerConfiguration/ContainerConfiguration.html#//apple_ref/doc/uid/TP30000102-BBCIDBBE) explains how to configure the transaction manager, the persistence manager, and the EJB container in your client applications.
- [Configuration Reference](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_JavaBeans/ConfigurationReference/ConfigurationReference.html#//apple_ref/doc/uid/TP30000103-BBCIDBED) provides explanations of the XML elements used in the configuration files of client applications.
- [Document Revision History](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_JavaBeans/RevisionHistory/RevisionHistory.html#//apple_ref/doc/uid/TP30000104-BAJJHJBG), lists changes made from previous editions of the document.

To get the most out of this document you should be an experienced WebObjects application developer. In particular, you need to know how to create applications using Project Builder and be familiar with the layout of a Project Builder project. To make use of enterprise beans in an application, you are required to edit configuration files written in XML; therefore, you should be familiar with XML’s rules and syntax.

To streamline your learning experience, you can take advantage of the companion resources that are included with this document in the `databases`, `models`, and `projects` directories in your hard disk or in the TAR file that you can download from [http://developer.apple.com/documentation/WebObjects/index.html](https://developer.apple.com/documentation/WebObjects/index.html).

If you need to learn the basics about developing WebObjects applications, you can find pertinent documents and resources in [http://developer.apple.com/webobjects](https://developer.apple.com/webobjects).

If you need to learn about EJB development, these books provide you introductory information as well as development guidelines:

- _Enterprise JavaBeans_ (O’Reilly)
- _Professional EJB_ (Wrox Press)
- _Applying Enterprise JavaBeans: Component-Based Development for the J2EE Platform_ (Addison-Wesley)

WebObjects uses open-source implementations of the EJB container, the object request broker, the transaction manager, and the persistence manager. For details about those implementations in WebObjects, consult the following resources:

- __OpenEJB__: Open-source EJB container system. For detains, see [http://OpenEJB.sourceforge.net](http://openejb.sourceforge.net/).
- __OpenORB__: Open-source implementation of the Common Object Request Broker Architecture. For information, see [http://OpenORB.sourceforge.net](http://openorb.sourceforge.net/).
- __Tyrex Transaction Manager__: Open-source J2EE transaction manager. See [http://Tyrex.sourceforge.net](http://tyrex.sourceforge.net/) for more information.

[Next](https://developer.apple.com/library/archive/documentation/WebObjects/Enterprise_JavaBeans/Introduction/Introduction.html)

