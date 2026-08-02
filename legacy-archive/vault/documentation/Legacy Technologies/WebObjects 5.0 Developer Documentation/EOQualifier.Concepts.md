---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/Concepts/EOQualifierConcepts.html
archived_at: '2026-07-15T08:13:45.136577Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Classes/Art/up.gif)](../../EOControlTOC.md)

# EOQualifier.Concepts

## Creating a Qualifier

As described above, there are several EOQualifier subclasses, each of which represents a different semantic. However, in most cases you simply create a qualifier using the EOQualifier static method __qualifierWithQualifierFormat__:, as follows:

> ```
> EOQualifier qual = Qualifier.qualifierWithQualifierFormat("lastName = 'Smith'", null);
> ```

The qualifier or group of qualifiers that result from such a statement is based on the contents of the format string you provide. For example, giving the format string "lastName = 'Smith'" as an argument to qualifierWithQualifierFormat returns an EOKeyValueQualifier object. But you don't normally need to be concerned with this level of detail.

The format strings you use to create a qualifier can be compound logical expressions, such as "firstName = 'Fred' AND age < 20". When you create a qualifier, compound logical expressions are translated into a tree of EOQualifier nodes. Logical operators such as AND and OR become EOAndQualifiers and EOOrQualifiers, respectively. These qualifiers conjoin (AND) or disjoin (OR) a group of sub-qualifiers. This is illustrated in [Figure 0-1](#apple-ijbesqsgincus), in which the format string "salary > 300 AND firstName = 'Angela' AND manager.name = 'Fred'" has been translated into a tree of qualifiers.

__Figure 0-1 EOQualifier Tree for 'salary > 300 AND firstName = "Angela" AND manager.name = "Fred"'__

![[image: Art/QualiferTree.GIF]](Art/QualiferTree.GIF)

The __qualifierWithQualifierFormat__ method can't be used to create an instance of EOSQLQualifier. This is because EOSQLQualifier uses a non-structured syntax. It also requires an entity. To create an instance of EOSQLQualifier, you'd use a statement such as the following:

> ```
> EOQualifier myQual = new EOSQLQualifier(myEntity, myFormatString);
> ```

## Constructing Format Strings

As described above, you typically create a qualifier from a format string by using qualifierWithQualifierFormat. This method takes as an argument a format string somewhat like that used with the standard C __printf()__ function. The format string can embed strings, numbers, and other objects using the conversion specification %@. The second argument to qualifierWithQualifierFormat is an array that contains the value or result to substitute for any %@ conversion specifications. This allows qualifiers to be built dynamically. The following table lists the conversion specifications you can use in a format string and their corresponding data types.

|  |  |
| --- | --- |
| __Conversion Specification__ | __Expected Value or Result__ |
| %@ | It can either be an object whose __toString__ (or __description__) method returns a key (in other words, a String), or a value object such as an String, Number, java.util.CalendarDate, and so on. |
| %% | Results in a literal % character. |

|  |  |
| --- | --- |
| __Conversion Specification__ | __Expected Value or Result__ |
| %s | A constant C string (__const char \*__). |
| %d | An __int__. |
| %f | A __float__ or __double__. |
| %@ | An __id__ argument. The behavior of this conversion specification depends on its position. It can either be an object whose description method returns a key (in other words, an NSString), or a value such as an NSString, NSNumber, NSCalendarDate, and so on. |
| %% | Results in a literal __%__ character. |

If you use an unrecognized character in a conversion specification (for example, %x), an exception is thrown.

For example, suppose you have an Employee entity with the properties __empID__, __firstName__, __lastName__, __salary__, and __department__ (representing a to-one relationship to the employee's department), and a Department entity with properties deptID, and name. You could construct simple qualifier strings like the following:

> ```
> lastName = 'Smith'
> salary > 2500
> department.name = 'Personnel'
> ```

The following examples build qualifiers similar to the qualifier strings described above, but take the specific values from already-fetched enterprise objects:

> ```
> Employee anEmployee;    // Assume this exists.
> Department aDept;       // Assume this exists.
> EOQualifier myQualifier;
> NSMutableArray args = new MutableVector();
>
> args.addObject("lastName");
> args.addObject(anEmployee.lastName());
> myQualifier = EOQualifier.qualifierWithQualifierFormat("%@ = %@", args);
>
> args.removeAllObjects();
> args.addObject("salary");
> args.addObject(anEmployee.salary());
> myQualifier = EOQualifier.qualifierWithQualifierFormat("%@ > %f", args);
>
> args.removeAllElements();
> args.addElement("department.name");
> args.addElement(aDept.name());
> myQualifier = EOQualifier.qualifierWithQualifierFormat("%@ = %@", args);
> ```

The enterprise objects here implement methods for directly accessing the given attributes: __lastName__ and __salary__ for Employee objects, and __name__ for Department objects. Note that unlike a string literal, the %@ conversion specification is never surrounded by single quotes:

> ```
> // For a literal string value such as Smith, you use single quotes.
> EOQualifier.qualifierWithQualifierFormat("lastName = 'Smith'", null);
>
> // For the conversion specification %@, you don't use quotes
> args.removeAllElements();
> args.addElement("Jones");
> EOQualifier.qualifierWithQualifierFormat("lastName = %@", args);
> ```

Typically format strings include only two data types: strings and numbers. Single-quoted or double-quoted strings correspond to String objects in the argument array, non-quoted numbers correspond to Numbers, and non-quoted strings are keys. You can get around this limitation by performing explicit casting.

The operators you can use in constructing qualifiers are =, ==, !=, <, >, <=, >=, "like", and "caseInsensitiveLike". The __like__ and __caseInsensitiveLike__ operators can be used with wildcards to perform pattern matching, as described in ["Using Wildcards and the like Operator" on page 99](#apple-ijbesqsjijaue).

## Checking for NULL Values

To construct a qualifier that fetches rows matching NULL, use either of the approaches shown in the following example:

> ```
> NSMutableArray args = new NSMutableArray();
>
> // Approach 1
> EOQualifier.qualifierWithQualifierFormat("bonus = nil", null);
>
> // Approach 2
> args.addElement(NullValue.nullValue());
> EOQualifier.qualifierWithQualifierFormat("bonus = %@", args);
> ```

## Using Wildcards and the like Operator

When you use the __like__ or __caseInsensitiveLike__ operator in a qualifier expression, you can use the wildcard characters \* and ? to perform pattern matching, for example:

> ```
> @"lastName like 'Jo*'"
> ```

matches Jones, Johnson, Jolsen, Josephs, and so on.

The ? character just matches a single character, for example:

> ```
> @"lastName like 'Jone?'"
> ```

matches Jones.

The asterisk character (\*) is only interpreted as a wildcard in expressions that use the __like__ or __caseInsensitiveLike__ operator. For example, in the following statement, the character \* is treated as a literal value, not as a wildcard:

> ```
> "lastName = 'Jo*'"
> ```

## Using Selectors in Qualifier Expressions

The format strings you use to initialize a qualifier can include methods. The parser recognizes an unquoted string followed by a colon (such as __myMethod:__) as a method. For example:

> ```
> point1 isInside: area
> firstName isAnagramOfString: "Computer"
> ```

Methods specified in a qualifier are parsed and applied only in memory; that is, they can't be used in to qualify fetches in a database.

## Using EOQualifier's Subclasses

You rarely need to explicitly create an instance of EOAndQualifier, EOOrQualifier, or EONotQualifier. However, you may want to create instances of EOKeyValueQualifier and EOKeyComparisionQualifier. The primary advantage of this is that it lets you exercise more control over how the qualifier is constructed.

If you want to explicitly create a qualifier subclass, you can do it using code such as the following excerpt, which uses EOKeyValueQualifier to select all objects whose "isOut" key is equal to 1 (meaning `true`). In the excerpt, the qualifier is used to filter an in-memory array.

> ```
> // Create the qualifier
> EOQualifier qual = new EOKeyValueQualifier("isOut", EOQualifier.QualifierOperatorEqual,
>     new Integer(1));
>
> // Filter an array and return it
> return Qualifier.filteredVectorWithQualifier(allRentals(), qual);
> ```

filteredArrayWithQualifier is a method that returns an array containing objects from the provided array that match the provided qualifier.

## Creating Subclasses

A custom subclass of EOQualifier must implement the EOQualifierEvaluation interface if they are to be evaluated in memory.

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Classes/Art/up.gif)](../../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
