---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.b.html
archived_at: '2026-07-15T08:10:01.080279Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Caching%20an%20Entity%27s%20Objects.md) [!](Localizing%20a%20WebObjects%20Application.md)

#   Mixing Languages in an Application

##  Synopsis

Describes how to mix Objective-C, Java, and WebScript in a WebObjects application.

##  Discussion

WebObjects supports three programming languages: Objective-C, Java, and WebScript. Objective-C is a fully compiled object-oriented version of C, and the language in which WebObjects and its associated frameworks are written. WebScript is an object-oriented scripting language similar to Objective-C that expedites the development of dynamic Web applications. WebObjects also provides WebObjects Framework and Enterprise Objects Framework APIs for the increasingly popular Java language.

It is sometimes necessary to mix one or more of these programming languages in a WebObjects application. For example, programmers may wish to program in Java and also use custom Objective-C frameworks already employed in other applications.

Note that WebObjects does not support the mixing of these languages in the same source code file. However, objects are accessible from non-native languages, and appear as if they were native to those languages.

From within a WebObjects application, Objective-C, Java, and WebScript can be mixed in the following ways:

- 

  Accessing Java objects from WebScript
- 

  Accessing WebScript objects from Java
- 

  Accessing Objective-C objects from Java
- 

  Accessing Java objects from Objective-C
- 

  Accessing WebScript objects from Objective-C
- 

  Accessing Objective-C objects from WebScript

This document provides examples for the most commonly used combinations of languages.

###  Accessing Objective-C Objects From WebScript

WebScript is very similar to Objective-C and shares a subset of the same syntax. In WebScript, you create and use Objective-C objects much as you would in Objective-C. You generally don't have to worry about retaining and releasing objects as WebScript automatically retains all instance variables for the life of the object that owns them and releases instance variables when the object owning the instance variables is released. The only exception is when you perform a mutable copy on an object--you must explicitly release the copied object.

Another difference is that WebScript does not require pointers to objects, nor does it require specifying class names in variable declarations, although it will parse such syntax in your code and ignore it. This feature eases the conversion between WebScript and Objective-C, allowing programmers to develop with a scripting language and deploy with a compiled language. Following are some code examples of using Objective-C objects in WebScript.

```

//Main.wos
id array1, array2;                    //you can declare ivars with id type
NSMutableArray *array2;               // or you can use the class type
array1=[[NSMutableArray alloc] init]; //no autorelease is needed
array2=[NSMutableArray new];          //use this method instead of alloc/init
                                      // to avoid some bugs in WebScript
array3=[[array1 mutableCopy] autorelease];  //autorelease will release
                                      // mutable copy when Main is released
```


###  Accessing WebScript Objects From Objective-C

Accessing WebScript objects and methods from Objective-C is simple and straightforward. Beware: changing your method names and arguments is effortless in WebScript but can also break any compiled code that accesses those WebScript methods.

Invoking methods in scripted WOApplication or WOSession objects from Objective-C is straightforward using the following code.

```

[[WOApplication application] myScriptedMethod];
[[[WOApplication application] session] myScriptedMethod];
```


Invoking methods in scripted WOComponents from Objective-C is not so straightforward because the Objective-C object needs to access the instantiated copy of the WOComponent. This can be done in one of two ways:

- 

  The WebScript WOComponent can save itself in the session dictionary.
- 

  The Objective-C object can locate and create the WOComponent's class using the WOResourceManager method
  pathForResourceNamed:inFramework:languages:
  to locate the component and
  scriptedClassWithPath:
  to get the class. Then it can allocate and initialize the WOComponent to use it, or call its static methods

Note that the two ways to access an instantiated copy of a WOComponent will work for any class. The following code example shows how to access a scripted WOComponent using the session dictionary.

```

//Main.wos -- save self in the session
[[self session] setObject:self  forKey:"@Main"];
```



```

//MyObject.m -- access the saved component from the session dictionary
WOComponent* aClass=[[self session] objectForKey:"@Main"];
```


The following code example shows how to instantiate a scripted WOComponent directly from Objective-C.

```

NSString* path=[[[WOApplication application] resourceManager]
    pathForResourceNamed:@"MyClass.wos" inFrameWork: nil
    languages: [[[self context] request] languages]];
Class scriptedClass=[[WOApplication application] scriptedClassWithPath:path];
MyClass* aClass=[[[testClass alloc] init] autorelease];
[aClass doSomething];
```


To avoid compiler warnings, you may want to declare the methods of the scripted class or component as an interface. Add these lines to the Objective-C object's implementation file (.m).

```objc

@interface TestClass
-(void)setMyVar:(NSString*)aVar;
-(void)doSomething;
@end
```


###  Mixing Java, WebScript, and Objective-C WOComponents

WebObjects allows you to mix WOComponents written in Java, Objective-C, and WebScript in a single application.

Code written in WebScript and Objective-C based WOComponents can access the instance variables (via accessor methods or key-value coding) and methods in each other, as explained in the two previous sections of this topic.

Code written in WebScript or Objective-C WOComponents can access the properties of Java components through key-value coding and the methods in Java WOcomponents by directly invoking them. Consider the following Java WOComponent:

```

//JavaPage.java
public class JavaPage extends WOComponent {
    public String aVar;
    public void aMethod1(String aValue){
        aVar=aValue;
    }
}
```


From a WebScript Component, first you create the new Java page instance, and then invoke its methods before returning the page:

```

//Main.wos
id var1;
-anAction{
    id page=self.application().pageWithName("JavaPage");
    [page aMethod1:@"Some String"];
    [page takeValue:@"another string" forKey:@"aVar"];
    return page;
}
```


When accessing a WebScript or a non Java-wrapped Objective-C WOComponent from a Java WOComponent, you can only create the page instance and set its properties using key-value coding. See the next section for an explanation of Java wrapping. The following example shows how to access properties in WebScript or Objective-C based WOComponents from a Java Component.

```

//JavaPage.java
public class JavaPage extends WOComponent {
    public String var1;
    public void aMethod1(String aValue){
        //WebScript component
        Component page=this.application().pageWithName("Main");
        page.takeValueForKey("some string","var1");
        var1= page.valueForKey("var1");
    }
}
```


###  The Java Bridge

The Java bridge provides a connection between the Objective-C object model and the Java object model. The Java bridge allows you to write code in one language that references an object from the other language. Classes in one language appear as classes in the other. Objective-C protocols appear as Java interfaces, and vice versa. Exceptions raised in Java are caught and converted into NSExceptions, which can then be handled in Objective-C.

Making Objective-C classes, methods, and protocols available in Java code is called wrapping because you create a Java wrapper for the Objective-C class (see the section, "Accessing Objective-C Objects from Java").

The Java bridge offers the following features:

- 

  It exposes Objective-C classes as Java classes that can be directly subclassed.
- 

  Java objects are passed across the bridge to Objective-C, where they are manipulated by the code as if they were Objective-C objects.
- 

  Some Java classes (such as String and Number) are mapped to Objective-C classes (such as NSString and NSNumber). Objects of these classes are transparently "morphed" into each other as they cross the bridge between the Java and Objective-C worlds.
- 

  Developers need not worry whether a class is written in Java or Objective-C. The bridge transparently loads any needed Objective-C framework whenever a bridged class is used.

The Java bridge currently supports Sun's Java Virtual Machine under Windows NT 4.0 and Solaris only. Other Java virtual machines can be supported in the future.

###  Accessing Java Objects From Objective-C and WebScript

WebScript objects can transparently instantiate most Java objects and invoke Java methods because of the Java bridge.

```

//WebScript code
aJavaObject=[MyJavaObject new];
[aJavaObject doSomething:arg1 foo:arg2];
```


The preceding WebScript maps to the following Java code.

```

//Java code
MyJavaObject aJavaObject=new MyJavaObject();
AJavaObject(arg1,arg2);
```


Similarly, Objective-C objects can transparently instantiate most Java objects and invoke Java methods because of the Java bridge.

```

//Objective-C code
Class testJavaObject = NSClassFromString(@"com.kelly.TestJavaObject");
aJavaObject=[testJavaObject alloc] init];
[aJavaObject doSomething:arg1 foo:arg2];
```


Invoking constructors and static methods on Java objects from Objective-C is a little more work and involves using some of the functions and methods in the ObjCJava framework. To invoke such methods from WebScript, you need to implement them in an Objective-C class, then invoke those Objective-C methods from WebScript.

####  WebScript_(Continued)_

```objc

//Test.m
#import "Test.h"
#import "NSJavaObject.h"
#import "vm-sun.h"
#import <JavaVM/JavaVM.h>
#import <Foundation/Foundation.h>
@interface MyJavaObject:NSObject
-(NSString)getString;
@end
@implementation Test
-(void)doit{
    Class javaClass;
    id anId;
    unsigned int methodCnt,i;
    const char* tmp;
    JAVAMethod amethod,methd;
    JAVAHandle ahandle,retHandle;
    JAVAClass aclass;
    MyJavaObject* instance;
    NSLog(@"In Test.m");
    javaClass = NSClassFromString(@"MyJavaObject");
    //invoke the constructor  public MyJavaObject(String s) using
    // macros included in the header vm-interface.h
    instance = [javaClass newWithSignature:
        [NSString stringWithCString:NSJSIG_METHOD
        ( NSJSIG_CLASS("java/lang/String") )], @"Hi!"];
    //invoke the method  public String getString() on MyJavaObject
    NSLog(@"%@",[instance getString]);
    //Fun with the bridge
    aclass=JAVAFindClass(EE(), "java/lang/String");
    //list all the methods & signatures for java.lang.String
    methodCnt=JAVAMethodCount(EE(),aclass);
    NSLog(@"Java class:%s has %d methods",
        JAVAClassName(EE(),aclass),methodCnt);
    for(i=0;i<methodCnt;i++) {
        methd=JAVAMethodAtIndex(EE(), aclass, i);
        tmp=JAVAMethodName (EE(), methd);
        tmp1=JAVAMethodSignature (EE(), methd);
        NSLog(@"Method:%s signature:%S",tmp,tmp1);
    }
    //to invoke the static method 'valueOf(int i)' on java.lang.String
    // first find the method
    amethod= JAVAStaticMethodLookup (EE(),aclass,"valueOf",
        "(I)Ljava/lang/String;");
    //pass in the method args here and invoke using this
    // convenience c func I wrote
    retHandle=InvokeJavaStaticMethodWithArgs(EE(),aclass,amethod,"%d",2);
    //you can see here it returned a java.lang.String
    NSLog(@"return class:%s",JAVAClassName(EE(),
        JAVAClassOfObject (EE(),retHandle)));
    //convert the handle to an NSObject and print the strings value
    anId=NSJavaHandleToId(retHandle);
    NSLog(@"JAVAStaticMethodInvoke return class:%s value:%@",tmp,anId);
}
@end
//this convienience function passes in the va_list
JAVAHandle InvokeJavaStaticMethodWithArgs(void *env,void *aclass,
    void *amethod,char* fmt, ...) {
    va_list ap;
    JAVAHandle jHandle;

    va_start(ap, fmt);
    jHandle=JAVAStaticMethodInvoke(env, aclass, amethod, 0, ap);
    va_end(ap);
    return jHandle;
}
```


###  Accessing Objective-C Objects From Java

Objective-C objects that are not wrapped as a special class appear as NSObjects in Java. You can use key-value coding to access the methods that are key-value coding compliant. If you require a more explicit wrapping, you can employ the Java bridge, which converts Objective-C classes, methods, and protocols to Java classes, methods, and interfaces, respectively.

The following steps describe the wrapping process:

Create a Java Wrapper project using Project Builder.

1. 

   Add your Objective-C framework to the project.
2. 

   Determine which Objective-C entities (classes, methods, and protocols) you want to expose in Java.

These entities must be packaged in a framework.

1. 

   Identify a single header (.h) file that declares (either directly or indirectly through importing other headers) all the Objective-C entities that you want to expose.

This header file can be one that already exists in your framework. Alternatively, you can create a header yourself and have it import the other headers you need.

1. 

   Use the WrapIt tool to create a .jobs file, save the file, and add it to your Java Wrapper project under Other Sources.
2. 

   Compile the Java Wrapper project. This creates Java-wrapped versions of your Objective-C objects, as Java classes.

The first step is to create the Java Wrapper project using Project Builder and add your Objective-C framework to the project under Frameworks. The next several steps involve using the WrapIt tool to choose which objects, methods, and protocols to expose in Java. WrapIt creates the
.jobs
file for you. Consider the following Objective-C header file:

```objc

//MyObject.h
@interface MyObject : NSObject
{
    NSString* _string;
}
-(id)init;
-(id)initWithString:(NSString*)aString;
-(void)setString:(NSString*)aString;
-(NSString*)mangleString:(NSString*)aString;
@end
```


Import the header file into WrapIt by dragging it into the file well at the bottom of the screen. Select which methods you want to expose and which methods you want to expose as constructors. Save the
.jobs
file, and place it in the Other Sources bin in your Java Wrapper project. Build the project.
MyObject.dll
(on Windows NT) and
MyObject.class
, the wrapped Objective-C class, are created.

MyObject.class
can now be referenced in your Java code just like any other Java class. The following figure shows what the class looks like in the Java Browser application:

```

//Public methodsMyObject.java
public class MyObject
    extends com.apple.yellow.foundation.NSObject
{
    public MyObject ();
    public MyObject (java.lang.String);
    public void setString (java.lang.String);
    public native java.lang.String mangleString (java.lang.String);
}
```


Here is a comparison of both objects and how they are mapped:

####  Objective-C Code

```objc

Objective-C Class_Java Class______
-(id)init;
-(id)initWithString:(NSString*)aString;
-(void)setString:(NSString*)aString;
-(NSString*)mangleString:(NSString*)aString;
NSString* _string;
public MyObject ();
public MyObject (java.lang.String);
public void setString (java.lang.String);
public native java.lang.String mangleString (java.lang.String);
No Mapping__
```


!Note Instance variables in Objective-C classes cannot be mapped directly to Java; you
must supply accessor methods to set and return them.!

##  See Also

##  Questions

- 

  How do I mix Objective-C and Java in a WebObjects application?
- 

  How do I mix WebScript and Java in a WebObjects application?
- 

  How do I mix Objective-C and WebScript in a WebObjects application?

##  Keywords

- 

  Java
- 

  Bridge
- 

  WebScript
- 

  Objective-C
- 

  Mixing
- 

  Languages

##  Revision History

10 July, 1998. Kelly Kazem. First Draft.

19 November, 1998. Clif Liu. Second Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Caching%20an%20Entity%27s%20Objects.md) [!](Localizing%20a%20WebObjects%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
