---
title: Using the Java Bridge
apple_id: TP40001404
resource_type: Guide
platform: Java
topic: Cross Platform
technology: null
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.5.html
archived_at: '2026-07-15T07:16:25.026777Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Using the Java Bridge](Legacy%20Documentclose%20button.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/index.html)  __>__  [Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/index.html) __>__
Using the Java Bridge

---

# Legacy Documentclose button

__Important:__
The information in this document is obsolete and should not be used for new development.

[Previous](Legacy%20Documentclose%20button-6.md) | [PDF](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.pdf)

[Using the Java Bridge](Legacy%20Documentclose%20button.md)

#  Wrapping Objective-C Frameworks

The Java bridge allows you to take existing Objective-C code and make it accessible to Java. To do so, follow these steps:

1. Determine which Objective-C entities (types, classes, methods, and protocols) you want to expose in Java.

   These entities must be packaged in a framework (or possibly more than one).
2. 

   Identify a single header (`.h`
   ) file that declares, either directly or indirectly through importing other headers, all the Objective-C entities that you want to expose. You'll specify this header when you edit the `.jobs`
   file in step 6 below.

   This header file can be one that already exists in your framework. Alternatively, you can create a header yourself and have it import the other headers you need. In particular, you'll do this when you add extra code to your Objective-C classes.
3. 

   Create a _Java Wrapper project_
   using Project Builder. See the next section for more information.
4. 

   Add your framework to the project.
5. 

   Optionally, add extra Objective-C code to your project. See [Modifying Your Code](#apple-ijdugqseijeum)
   for information on when you might need to do this.
6. 

   Edit the `.jobs`
   file in your project to specify which entities should be exposed, and the Java names that should correspond to them.

   This process is called _mapping_
   and is described in [Name Mapping](#apple-ijdugqscinbuo)
   . You use the `.jobs`
   file in your project to specify the mapping information. [Editing the Specification File](#apple-ijdugrcgjfbem)
   describes the details of working with the `.jobs`
   file.
7. 

   Build the project.

   The build process invokes the `bridget`
   tool, which outputs the files needed to use the Objective-C classes in your Java code. See [Building the project](#apple-ijdugrciirceu)
   .

##  Creating a Java Wrapper Project

In Project Builder:

1. Choose Project-> New.
2. 

   In the New Project panel, select Java Wrapper from the pop-up list.
3. 

   Specify the project path by typing it in the text box or by clicking Browse to navigate to it.
4. 

   Click OK.

The newly created project contains the following files of interest:

- The Other Sources suitcase contains a skeleton specification (`.jobs`
  ) file.
- 

  The Frameworks suitcase contains the Foundation framework by default. You must add the framework you are wrapping to the project.

##  Name Mapping

This section provides some background information you'll need in order to properly edit your `.jobs`
file.

The Java bridge maintains a table that maps Objective-C selectors to Java method names. By default, the bridge maps Objective-C selectors to Java by using the first keyword only. For example, the method `doThis`
would map to `doThis()`
in Java. If this is what you want, you don't need to specify an explicit mapping.

The Java bridge also lets you overload Java method names, as long as each one has a unique arguement list, so the methods `doThis:withThat:`
and `doThis:withSomethingElse:`
can both map to `doThis()`
in Java. However, as of press time, the bridge still had limitations with overloading, so in some cases you may need specify different Java names, say, `doThisWithThat()`
and `doThisWithSomethingElse()`
.. For more information, check the files in `/System/Documentation/Developer/ReleaseNotes/`
.

There are some other restrictions on name mapping:

- A single Objective-C selector can't be mapped to different Java method names for different classes or interfaces. For example, If you map `foo:`
  to `javaFoo()`
  in a given class, any method named `foo:`
  in another class must map to `javaFoo().`
- 

  Different Objective-C selectors can't be mapped to the same Java method name. For example, if you map `foo:`
  to `javaFoo()`
  in a given class, you can't map `fooBar:`
  to `javaFoo()`
  in another class.
- 

  In Objective-C, it's possible for an instance method to have the same name as a class method, while in Java, class (static) and instance methods share the same name space. Therefore, if an Objective-C class has methods `-foo`
  and `+foo`
  , you must map at least one of them to a different name in Java.

Objective-C initialization methods should be exported in Java as constructors, not as instance methods. This allows you to use the `new`
operator in Java to allocate and initialize the operator.

You can expose multiple initialization methods as constructors. For example, suppose the Foo class has two initialization methods: `init`
and `initWithString:(NSString*)`
. The bridge creates the appropriate Java constructors based on the argument types: `init`
becomes the constructor `Foo()`
in Java, and `initWithString:`
becomes `Foo(String s)`
.

##  Editing the Specification File

The specification (`.jobs`
) file shows how the Objective-C class is exposed in Java. It allows you to choose which Objective-C classes, methods, types, and protocols you want to expose, and the names they should have on the Java side.

The `.jobs`
file also allows you to add specific code to a Java class or interface. This can be used to define constants corresponding to enumerated types used in Objective-C, or simply to provide extended functionality in the Java world.

The `.jobs`
file that is created by default with a Java wrapper project looks like this:

##### The .jobs file in a new project

!

There are two ways to edit a `.jobs`
file:

- Use the WrapIt application, which lets you graphically specify the relationships between Objective-C and Java classes. It's in the directory `System/Developer/Applications`
  and you can find documentation on it in `System/Documentation/Developer/ReleaseNotes`
  .
- 

  Edit it manually within Project Builder.

Note that if you use the WrapIt application, you should not manually edit the `.jobs`
file it creates

The table below lists the keywords that the specification file understands, and shows examples each one.

##### Syntax of .jobs file

**name**
: 

The name of the package, which comes from the project name (you shouldn't change it). It's also used for the name of the library initialization file, for example, `SimpleWrapper-init.m`
.


```
name SimpleWrapper
```


**header**
: 

Specifies the header file that `bridget`
should read to parse the Objective-C `@interface`
declarations. You can only specify one header file.


```
header MyFramework/Foo.h
```


**import**
: 

Specifies other `.jobs`
files that `bridget`
should include for class mappings, type definitions, and so on.


```
import FoundationJava.jobs
```


**stub-import**
: 

Specifies header files that you want to output as `#import`
statements in the generated stub code.


```
stub-import MyHeader.h
```


**selector**
: 

Specifies any non-default mappings between Objective-C selectors and Java method names. (The default is to use the Objective-C name before the colon as the Java name.) These mappings apply to all classes. __Note:__
Put all of the mappings under a single `selector`
specification.


```
selector
    -defineClass:withName: = defineClassWithName
    -pathForResource:ofType: = pathForResourceType
```


**protocol**
: 

Exposes an Objective-C protocol as a Java interface. Use one `protocol`
directive for each protocol. You must specify all methods within the protocol that you want exposed. __Note:__
Constructors are not allowed in Java interfaces. Therefore, don't specify initialization methods in a protocol; you must specify them as constructors in each class that uses the protocol (refer to the `class`
keyword for more information).

```
protocol MyProtocol = com.myFirm.whatever.myInterface
-doThis:
-doThat:
-doSomethingElse:
```


**class**
: 

Specifies the classes that should be exposed and the methods in each class. Use one `class`
specification for each class. In the example here, the Objective-C class MyObjCClass is exposed as com.myFirm.whatever.myJavaClass. The `implements`
directive specifies an Objective-C protocol that the class conforms to; all methods in this protocol are exposed. __Note:__
This protocol must also be exposed as a Java interface using `protocol`
.

All additional methods you want to expose must be shown explicitly. Objective-C class methods (such as `+myClassMethod`
) are mapped to Java static methods. Objective-C instance methods (such as `-myInstanceMethod:`
) are mapped to Java instance methods. The `constructor`
directive is used to map Objective-C initialization methods to Java constructors.


```
class MyObjCClass = com.MyFirm.Whatever.MyJavaClass
    implements MyProtocol
    -myInstanceMethod:
    -myOtherInstanceMethod:withArguments:
    +myClassMethod
    constructor -init
    constructor -init:withSomething:
```


Within the `class`
specification, you can specify additional Java code to be added to the class. In the following example, Java constants are declared, corresponding to enumerated types in Objective-C:


```
@{
    public static final int InnerJoin = 0;
    public static final int FullOuterJoin = 1;
@}
```


You can also specify statements that will appear at the top or bottom of a Java package:


```objc
@top {
    import com.yourFirm.whatever.*
@}

@end {
    private class notSeenAnywhereElse {
        int secret() { return 2001; }
@}
```


**type**
: 

Used to map Objective-C types to Java basic types or classes.

```
type
    NSTimeInterval = double
    NSComparisonResult = int

    NSMyStruct = com.myFirm.myJavaClass using _f1 _f2 _f3
struct-size 16
```


This last form is designed to map Objective-C structs to Java classes. If you need to do this, you must provide three conversion functions: two that convert the struct to a Java object (by reference and by value), and one that converts the Java object to the Objective-C struct, as in the following prototypes:


```
JAVAHandle _f1(NSMyStruct *n, int *structSize);
JAVAHandle _f2 (NSMyStruct n);
NSMyStruct _f3 (JAVAHandle myJavaObj);
```


**map**
: 

Specifies routines for converting ("morphing") Objective-C classes to Java classes and vice versa.

```
map
    NSNumber = java.lang.Number using _NSNumberToJavaNumber
_JavaNumberToNSNumber
```


**name**
: 

The name of the package. It's used for the name of the library initialization file as well, for example, `SimpleWrapper.m`
.

```
name SimpleWrapper
```


**preinit-callout**
: 

Allows you to specify a function to execute before the bridge's standard initialization code (which sets up the Java-to-Objective-C mappings). 

```
preinit-callout your_pre_initialization_function
```


**postinit-callout**
: 

Allows you to specify a function to execute after the bridge's standard initialization code.

```
postinit-callout your_post_initialization_function
```


##  Building the project

The `bridget`
tool uses the `.jobs`
file to generate Java classes and interfaces for a given set of Objective-C entities.

When you build the project, the following files are generated:

- A dynamic library containing the Objective-C classes and protocols packaged as Java classes and interfaces.
- 

  A `.java`
  file for each Objective-C class listed in the `.jobs`
  file.

  It contains declarations for all of the methods in the class, as well as a static initialization method that insures that the dynamic library is loaded the first time an object of the class is instantiated.
- 

  A C stubs file for each class listed in the `.jobs`
  file.
- 

  A file (_projectName_
  `-init.m`
  ) containing initialization code for the Objective-C classes. This code is run the first time the dynamic library is loaded, and sets up the Java-to-Objective-C mappings.

##  Modifying Your Code

Occasionally, differences between Objective-C and Java may require you to change your Objective-C framework in order for it to work properly with the bridge. Typically, changes are done by adding categories rather than changing the original classes. You add Objective-C `.m`
files to the Classes bucket and `.h`
files to the Headers bucket in your project.

The following sections describe some reasons why you might need to modify your code.

### Pointers

Java doesn't use pointers, while Objective-C (like C and C++) does. In some cases, you may need to change your code if an Objective-C method you are wrapping returns a pointer or takes a pointer as an argument.

- The bridge automatically converts a pointer to an object (such as an `NSArray*`
  ) to a Java object reference. Therefore, any method using an object pointer will work correctly without modification.
- 

  Pointers such as `int*`
  or `id*`
  or `void*`
  will not work. The Objective-C method must be changed.

In the following example, an Objective-C method uses pointers to return two values "by reference".


```
NSFoo value1:(int*)v1 value2:(int*)v2
```


In Java, values must be returned explicitly by value, so you need to rewrite this method. You can, for example, write separate methods to return each of the values and add them to the NSFoo class via a category, as follows:


```objc
@interface NSFoo(MyJavaExtensions)
- (int) value1; //returns first argument
- (int) value2; //returns second argument
@end

@implementation NSFoo(MyJavaExtensions)
- (int) value1 {
    int v1, v2;
    [self value1:&v1 value2:&v2]; //invokes original method
    return v1;
};
- (int) value2 {
    int v1, v2;
    [self value1:&v1 value2:&v2];
    return v2;
};
@end
```


Another option is to rewrite `value1:value2:`
as a single method whose return type is an NSDictionary that contains both values.

### Constructors

Normally, Objective-C initialization methods are mapped to Java constructors based on the number and types of arguments. A special cases arises when an Objective-C class has two initialization methods with the same argument types but different names (say, `initWithString:`
and `initWithPathName:`
, both taking an NSString). In this case, Java can't distinguish between the two needed constructors.

One solution is to create a "cover" method in Objective-C that takes an extra parameter and calls the correct initialization method depending on the value of the second parameter. This cover method is mapped to the Java constructor.

A similar approach is to write the cover method in Java. You expose the initialization methods as instance methods rather than constructors and add a custom pure Java constructor such as:


```
public Foo (String myString, boolean isPathName) {
    if (isPathName) {
        this.initWithPathName(myString);
    }
    else {
        this.initWithString(myString);
    }
}
```


This code can be added to a Java class in the `.jobs`
file. See the description of the `class`
keyword in [Editing the Specification File](#apple-ijdugrcgjfbem)

---

[Previous](Legacy%20Documentclose%20button-6.md) | [PDF
\xA9 1998 Apple Computer, Inc.](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Legacy/JavaBridge/JavaBridge.pdf)
