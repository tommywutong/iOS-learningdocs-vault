---
title: Hiding public methods from AppleScript in Java
apple_id: DTS10001384
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/java/java09.html
archived_at: '2026-07-18T02:29:41.143395Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > Porting](https://developer.apple.com/referencelibrary/Java/idxPorting-date.html)

|  |
| --- |
| Technical Q&A JAVA09Hiding public methods from AppleScript in Java |

|  |  |  |
| --- | --- | --- |
| ---   Q: I have several public methods in my class that I do not want exposed to AppleScript. Is there any way that I can specify this in my Java code, or do I have to do this by editing the `'aete`'?  A: You can do this easily in code. By creating a `BeanInfo` for your class, you may exclude both properties and methods from the automatically generated `'aete'` resource.  Given a class `Salad.java`:   |  | | --- | | ``` public class Salad {    public int  msgAmount; // we don't want this in our ingredients list public void setMsgAmount( int amount ) { msgAmount = amount; }    public int  getMsgAmount( ) { return msgAmount; }    public void addMSG( int amount ){ ... }                 // hide this too       ... }; ``` |   You can make a `SaladBeanInfo.java`:   |  | | --- | | ``` import java.beans.*; import java.lang.reflect.*; ```  ``` public class SaladBeanInfo extends SimpleBeanInfo {     public MethodDescriptor[ ] getMethodDescriptors()     {         MethodDescriptor md[ ] = new MethodDescriptor[1]; ```  ```         try         {            md[0] = new MethodDescriptor( getMethod( Salad.class,                "addMSG" ), pd );            md[0].setHidden( true );            return md;         }         catch ( IntrospectionException e )         {              e.printStackTrace();         }         return null;     }     public PropertyDescriptor[ ] getPropertyDescriptors()     {         PropertyDescriptor pd[ ] = new PropertyDescriptor[1];         try         {              pd[0] = new PropertyDescriptor(                 "msgAmount", Salad.class );              pd[0].setHidden( true );              return pd;         }         catch ( Exception e )         {              e.printStackTrace();         }         return null;      } ```  ```      Method getMethod( Class c, String methodName ) throws IntrospectionException     {         Method methods[ ] = c.getMethods();         for ( int i = 0; i < methods.length; i++ )         {             if ( methods[i].getName().equals( methodName ))             {                 return methods[i];             }         }         throw new IntrospectionException(                 "No such method \"" + methodName + "\"" );     } } ``` |    We first create a method descriptor and set the `isHidden` property to true by calling `setHidden( true )`. This will tell the introspector not to return information to the `'aete'` generator for this method. Thus, this method will not appear in the AppleScript dictionary for this application.  Hiding properties is a slightly different process, but is nonetheless quite straightforward. We create a `PropertyDescriptor` and call the inherited `setHidden( )` method from `java.beans.FeatureDescriptor`. In this manner, we can also prevent the scriptor (and health inspector) from knowing about this hidden property. |

#### [May 17 1999]

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

---
