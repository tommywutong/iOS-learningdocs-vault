---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.1d.html
archived_at: '2026-07-15T08:09:57.653191Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Creating%20Fetch%20Specifications%20Programmatically.md) [!](Creating%20Sort%20Orderings.md)

#   Creating EOQualifiers Programmatically

##  Synopsis

Describes the basics of programmatically building an EOQualifier.

##  Description

An EOQualifier specifies which objects to fetch from a database or filter in an array. It is the Enterprise Objects Framework equivalent to the SQL
WHERE
clause, but it is designed to work with graphs of objects rather than rows in a database. EOQualifiers are used in conjunction with EOSortOrderings to create EOFetchSpecifications. See the programming topic [Creating Fetch Specifications Programmatically](Creating%20Fetch%20Specifications%20Programmatically.md#apple-gm4tsmjz)
for more information about EOSortOrderings and EOFetchSpecifications.

The easiest way to create an EOQualifier is using the EOQualifier static method
qualifierWithQualifierFormat
, as follows:

```

EOQualifier qual = EOQualifier.qualifierWithQualifierFormat
  (formatString, args);
```


This method takes as an argument a format string somewhat like that used with the standard C
printf()
function. The format string can embed strings, numbers, and other objects using the conversion specification
%@
. The second argument to
qualifierWithQualifierFormat
is an NSArray that contains the value or result to substitute for any
%@
conversion specifications. This allows qualifiers to be built dynamically. To embed a percent sign (
%
) in the qualifier use
%%
. Note: If you use an unrecognized character in a conversion specification (for example,
%x
), an exception is thrown.

In Objective-C, the equivalent code looks like this:

```

EOQualifier qual;
qual = [EOQualifier qualifierWithQualifierFormat:
  formatString, arg1, arg2, ... ]
```


For example, suppose you have a Movie entity with the properties
title
,
category
,
revenue
,
dateReleased
, and
toMovieRole
(representing a to-many relationship to the movie's roles), and a MovieRole entity with a
roleName
property. Furthermore, you want to find all movies that start with a user-specified string in
searchTitle
and grossed more than a user-specified amount of money in
searchRevenue
. The following code builds an EOQualifier that finds these movies.

####  Building a qualifier (Java)

```

String searchTitle;     // Assume this exists
Integer searchRevenue;  // Assume this exists

String wildTitle = searchTitle + "*";
EOQualifier myQualifier;
NSArray args = new NSArray(new Object[] {wildTitle,"revenue",searchRevenue});
myQualifier = EOQualifier.qualifierWithQualifierFormat
    ("title caseInsensitiveLike %@ AND %@ < %@", args);
```

####  Building a qualifier (Objective-C)

```

NSString searchTitle;   // Assume this exists
int searchRevenue;      // Assume this exists

NSString wildTitle;
EOQualifier myQualifier;

wildTitle = [NSString stringWithFormat:@"%@*",searchTitle];
myQualifier = [EOQualifier qualifierWithQualifierFormat
    @"title caseInsensitiveLike %@ AND %@ < %d",
    wildTitle,@"revenue",searchRevenue];
```


Note that in Objective-C, the
%d
,
%f
, and
%s

printf()
formats are supported in addition to
%@
.

String literals are expressed in single quotes. However, the
%@
conversion specification is never surrounded by single quotes.

```

// For a literal string value such as Smith, you use single quotes.
EOQualifier.qualifierWithQualifierFormat("lastName = 'Smith'", null);

// For the conversion specification %@, you don't use quotes
args = NSMutableArray("Jones");
EOQualifier.qualifierWithQualifierFormat("lastName = %@", args);
```


The operators you can use in constructing qualifiers are
=
,
==
,
<>
,
<
,
>
,
<=
,
>=
,
like
, and
caseInsensitiveLike
. The
like
and
caseInsensitiveLike
operators can be used with wildcards to perform pattern matching, as described below.

###  Using Wildcards and the like Operator

When you use the
like
or
caseInsensitiveLike
operator in a qualifier expression, you can use the wildcard characters
\*
and
?
to perform pattern matching, for example:

```

"lastName like 'Jo*'"
```


matches Jones, Johnson, Jolsen, Josephs, and so on.

The
?
character just matches a single character, for example:

```

"lastName like 'Jone?'"
```


matches Jones.

The asterisk character (
\*
) is only interpreted as a wildcard in expressions that use the
like
or
caseInsensitiveLike
operator. For example, in the following statement, the character
\*
is treated as a literal value, not as a wildcard:

```

"lastName = 'Jo*'"
```


Note that when you combine wildcards with the
%@
conversion specification, you must put the wildcard in the argument and not the conversion:

```

// CORRECT:
keyword = "Jo";
NSArray args = new NSArray (keyword+"*");
EOQualifier myQualifier = EOQualifier.qualifierWithQualifierFormat
    ("lastName like %@",args);
```


The following code won't work:

```

// WRONG:
keyword = "Jo";
NSArray args = new NSArray (keyword);
EOQualifier myQualifier = EOQualifier.qualifierWithQualifierFormat
    ("lastName like %@*",args);
```

###  Joining Qualifiers

The EOAndQualifier and EOOrQualifier subclasses of EOQualifier can be used to form boolean combinations of qualifiers. For example, the EOAndQualifier is itself a qualifier that is the logical AND of its constituent qualifiers. In the following code,
myQualifier1
is equivalent to
myQualifier2
.

```

NSMutableArray args = new NSMutableArray();
args.addObject(EOQualifier.qualifierWithQualifierFormat
    ("title like 'S*'"));
args.addObject(EOQualifier.qualifierWithQualifierFormat
    ("revenue > 500000"));
EOAndQualifier myQualifier1 = EOAndQualifier(args);

EOQualifier myQualifier2 = EOQualifier.qualifierWithQualifierFormat
    ("title like 'S*' AND revenue > 500000");
```


The EONotQualifier forms the logical NOT of its constituent qualifier and can be used with EOAndQualifier and EOOrQualifier to form complex boolean qualifiers.

Using the boolean EOQualifier subclasses is often more convenient than using
qualifierWithQualifierFormat
when forming qualifiers by iterating over enumerated objects. An example is building keyword searches. The following code example builds a qualifier based on an NSArray of keywords. The qualifier filters the Movies database for all Talents that have all of the keywords in their names, the movie roles they star in, or the movies they star in.

```

NSArray keywords;   // Assume exists
NSMutableArray qualifierArray = new NSMutableArray();
Enumeration e = keywords.objectEnumerator();
while (e.hasMoreElements()) {
    String kw = e.nextElement();
    kw = "*" + kw + "*";
    String qualifierString =
        "firstName caseInsensitiveLike %@ OR " +
        "lastName caseInsensitiveLike %@ OR " +
        "toMovieRole.roleName caseInsensitiveLike %@ OR " +
        "toMovieRole.toMovie.title caseInsensitiveLike %@";
    EOQualifier tempQualifier = EOQualifier.qualifierWithQualifierFormat
        (qualifierString,new NSArray (new Object[] {kw,kw,kw,kw}));
    qualifierArray.addObject (tempQualifier);
}
EOQualifier qualifier = new EOAndQualifier(qualifierArray);
```

##  See Also

- 

  [Creating Fetch Specifications Programmatically](Creating%20Fetch%20Specifications%20Programmatically.md#apple-gm4tsmjz)
- 

  [Creating Sort Orderings](Creating%20Sort%20Orderings.md#apple-gm2tcmbu)

##  Questions

- 

  How do I programmatically create an EOQualifier?
- 

  How do I use wildcards with an EOQualifier?

##  Keywords

- 

  Qualifier
- 

  Wildcard
- 

  SELECT

##  Revision History

10 March, 1999. Clif Liu. First Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Creating%20Fetch%20Specifications%20Programmatically.md) [!](Creating%20Sort%20Orderings.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
