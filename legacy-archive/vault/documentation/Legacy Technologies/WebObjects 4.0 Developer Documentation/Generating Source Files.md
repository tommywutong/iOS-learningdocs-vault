---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/Entities4.html
archived_at: '2026-07-18T01:18:13.933722Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Working%20with%20Entities.md) [!Previous Section](Specifying%20an%20Enterprise%20Object%20Class.md)

# Generating Source Files

Once you finish specifying an enterprise object class, you can generate source files for it. However, at this stage of the development process, you may want to first create your project and design your application's user interface. Once you've created a project using Project Builder and included a model file in it, you can generate your source files and save them into the project.
You can create your enterprise object classes in either Objective-C or Java. To create an Objective-C class, use Property ! Generate Obj-C Files. To create a Java class, use Property ! Generate Java Files.
Additionally, there's a Property ! Generate Client Java Files. This command generates a Java class for use in the client-side of a Java Client web application.
Each command is described in more detail in the following sections.

## Generating Objective-C Source Files

To generate Objective-C code files for your enterprise object class:

- In the Model Editor, select the entity for which you have specified a class in the Entity Inspector.

EOModeler only permits you to create source files for entities for which you have specified a custom enterprise object class. In other words, you can't generate source files for EOGenericRecord.

- Choose Property ! Generate Obj-C Files or click the ! button in the toolbar.

EOModeler displays a Choose Class Name panel. If the model file is in a project, the Choose Class Name panel displays the project as the default destination.

- Choose a destination, supply a name for the files if you want, and click Save.

If you don't supply a name, the source files are named after the enterprise object class for which they are being generated and are given the appropriate extensions.

If you opened the model file from a project, an additional panel appears, confirming that you want to insert the files in your project.

Also, if you generate source files for an entity and files of the same name already exist, a panel is displayed asking if you want to cancel, overwrite, or merge the files. If you choose merge, the File Merge application starts with the old and new files displayed. You can then merge the files.

The end result of the Generate Obj-C Files command is:

- A header (__.h__) file that declares instance variables for all of the entity's class properties and declares accessor methods for those instance variables.
- An implementation (__.m__) file that provides basic implementations for the accessor methods.

For example, suppose you define an enterprise object class Movie. The instance variable declarations in the generated header file might resemble the following:

```
NSString *category;
NSCalendarDate *dateReleased;
NSDecimalNumber *language;
NSString *posterName;
NSDecimalNumber *revenue;
NSString *title;
id plotSummary;
Studio *studio;
NSMutableArray *directors;
NSMutableArray *roles;
```


Note that:

- The name of the generated class is the name you specified for the entity's Class Name characteristic.
- Instance variables that correspond to attributes are declared to be of the Objective-C value class specified in the model. For example, __revenue__ is declared as an NSDecimalNumber and __dateReleased__ is declared as an NSCalendarDate.
- Instance variables that represent to-one relationships are declared to be of type __id__ for destination objects represented with EOGenericRecord (such as __plotSummary__) or as instances of the custom class used to represent them (such as __studio__).
- Instance variables that represent to-many relationships (such as __directors__) are NSMutableArrays.

The corresponding implementation (__.m__) file for Movie includes an implementation for each of the accessor methods declared in the header file. For example, the methods for setting and returning the value of the instance variable __title__ are:

```objc
- (void)setTitle:(NSString *)value
{
    [self willChange];
    [title autorelease];
    title = [value retain];
}
- (NSString *)title { return title; }
```


## Generating Java Source Files

Generate Java Files is similar to generating Objective-C files. To generate a Java (__.java__) file for your enterprise object class, follow the steps in [Generating Objective-C Source Files](#apple-ge2tiojt), except that you choose Property ! Generate Java Files or click the ! button in the toolbar.

As with the Objective-C source files, a Java source file declares instance variables and provides basic implementations of accessor methods for those variables. And in Java:

- The name of the generated class is the name you specified for the entity's Class Name characteristic.
- Instance variables that correspond to attributes are declared to be of the Java value class specified in the model, which can be String, NSGregorianDate, Number, BigDecimal, NSData or a custom value class that you specify.
- Instance variables representing to-one relationships are declared to be of type EOEnterpriseObject for destination objects represented with EOGenericRecord or as instance of the custom class used to represent them. (EOEnterpriseObject is a Java interface defining basic enterprise object behavior; for more information, see the chapter "Designing Enterprise Objects" in the book _Enterprise Objects Framework Developer's Guide_ or the EOEnterpriseObject interface specification in _Enterprise Objects Framework Reference_).
- As with Objective-C, instance variables that represent to-many relationships (such as __directors__) are NSMutableArrays.

## Generate Client Java Files

Generate Client Java Files is similar to the other source generation commands. However, you only use this command when you're creating enterprise object classes to run on the client-side of a Java Client web application. (For a description of a Java Client application, see the chapter "What's Enterprise Objects Framework" in the book _Enterprise Objects Framework Developer's Guide_).
Using this and one of the other two source generation commands (either Objective-C or Java), you can create two versions of your enterprise object class. The different versions can have different class properties. For example, for security reasons, you might want to include social security number attribute in the server-side version of an enterprise object but exclude it from the client-side version.
To enable this distinction, you can specify whether an attribute is a Class Property (!) to be included in the server-side enterprise objects and also whether an attribute is a Client-Side Class Property (!) to be included in the client-side objects. For more information on setting these characteristics, see the chapter[Working with Attributes](Working%20with%20Attributes.md#apple-ge2tsojv).

To generate a Java (__.java__) file for a client-side version of your enterprise object class, follow the steps in [Generating Objective-C Source Files](#apple-ge2tiojt), except that you choose Property ! Generate Client Java Files.

As with the source files generated by the other commands, a Java source file declares instance variables and provides basic implementations of accessor methods for those variables. The client-side Java files are generated exactly like the server-side Java files, except:

- The name of the generated class is the name you specified for the entity's Client-Side Class Name characteristic. If you haven't specified a Client-Side Class Name, it uses the name you specified for the entity's Class Name characteristic.
- If the model file is in a project, the default destination for the files is the ClientSideJava.subproj. Consequently, you can name your server-side and client-side enterprise object classes with the same name. The two versions of your class reside in different name spaces at runtime, too. Even if your server-side class is a Java class, it descends from com.apple._yellow_.eocontrol.EOCustomObject, while the client-side class descends from com.apple.client._eocontrol_.EOCustomObject.
- Instance variables are generated only for attributes and relationships that are set as Client-Side Class Properties.

## Customizing Source File Generation

When you create a project with the type "EOApplication," it inserts three files into the project's Supporting Files suitcase: __EOInterfaceFile.template__, __EOImplementationFile.template__, and __EOJavaClass.template__. You can use these files to customize your __.h__, __.m__, and __.java__ file output, respectively. In their unmodified form these files match the source file generation scheme used by EOModeler.

[!Table of Contents](Working%20with%20Entities.md) [!Next Section](Creating%20a%20Subclass.md)
