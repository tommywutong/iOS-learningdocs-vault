---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/The_Rule_System.html
archived_at: '2026-07-15T08:12:23.535393Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Resolving_K_he_Property.md)[![Next](attachments/DirectToWeb/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Customizing/index.html)

## The Rule System

Direct to Web stores its configuration in the form of rules.
The following is an example of a rule:

```
((task = "query") and (not(attribute = null))
    and (attribute.valueClassName = "NSString")
    => componentName = "D2WQueryStringComponent"
```

A rule consists of five parts, of which three are shown in
the example:

- __a
  left-hand side__, which is separated from the right-hand
  side by "=>"

  The left-hand side specifies a condition
  that must be true for the rule to be a candidate to fire. In this
  case, the task must be "query", the attribute must not be `null` and
  its value must be an NSString.
- __a right-hand-side key__ (`componentName` in
  this case)

  The right-hand-side key must match the key the Direct
  to Web context is seeking for the rule to be a candidate to fire.
- __a right-hand-side value__ ("D2WQueryStringComponent"
  in this case)

  The right-hand-side value specifies the value
  for the right-hand-side key when the rule fires. It can be a constant
  value (as in this case) or a value computed by a method.
- __a priority__

  The priority helps
  Direct to Web decide which rule should fire when there are several candidates.
  See ["Deciding Which Candidate Should Fire"](#apple-ijauuqsdjfdui) for more information about the
  rule priority.
- __an assignment class specifier__

  The
  assignment class sets the value for the right-hand-side key when
  the rule fires. Assigning a constant value like "D2WQueryStringComponent"
  is done by the default assignment class, Assignment, defined in
  the Direct to Web framework. When the right-hand-side value is derived
  using a method, the assignment class specifies a class that contains
  the method.

### Deciding Which Candidate Should Fire

When the Direct to Web context asks for the value for a key,
there are typically several rules that can fire. For example, consider
the following rules to resolve the `componentName` key:

```
*true* => componentName = "D2WUneditable"

(task = 'inspect') => componentName = "D2WDisplayString"

((task = "inspect") and (attribute.valueClassName = "NSTimestamp"))
    => componentName = "D2WDisplayDate"
```

The left-hand side of the first rule is always true. Such
rules are useful for providing "fallback" values when all other
rules fail to fire. Note that if the left-hand side for the third rule
is true, all three rules are candidates for firing. The rule engine
must choose which rule will fire.

To make the choice, Direct to Web employs a priority system.
Each rule has a priority. The single rule with the highest priority
fires. By convention, the following priorities are used in Direct
to Web.

__|  |  |
| --- | --- |
| Priority | Description |__| 0-10 | Reserved for Direct to Web framework and fallback rules |
| 100-105 | WebAssistant rules |

If two or more rules have the same priority, the rule with
the most specific left-hand side (applying to the least number of
cases) fires. Direct to Web measures how specific a rule is by counting
the number of clauses joined by an _and_ operator;
the more clauses the rule has, the more specific it is. Clauses
joined by the _or_ operator count as a single
clause.

If two or more rules have the same priority and are equally
specific, Direct to Web arbitrarily chooses one.

The rule system resolves keys recursively. In other words,
the rule system can resolve a rule based on the outcome of another
rule. Consider a rule for the `pageName` key:

```
((look = "BasicLook") and (task = "query")) => pageName = "BASQueryPage"
```

The `look` key is
defined by a rule like this:

```
*true* => look = "BasicLook"
```

To resolve the `pageName` key,
the rule engine asks the Direct to Web context for values for the `look` and
the `task` keys. The Direct
to Web context then invokes the rule engine to resolve the `look` key.
This extra step isn't necessary for the task key; it's already
in the Direct to Web context's local dictionary. Although recursive
rules are powerful, they can hamper Direct to Web's performance.

To see the rules that fire as Direct to Web renders pages,
run your application with the switch `-D2WTraceRuleFiringEnabled
YES`.

### Rules and the Web Assistant

The Web Assistant defines rules that pertain to specific entities
and properties in your application, unlike the rules from the Direct
to Web framework. These rules have a priority of 100, which override
the default rules in the Direct to Web framework. Consequently,
if you want to define your own default rules that the Web Assistant
can override, you need to specify them with a priority between 11
and 99.

When you click Update in the Web Assistant window, the settings
are compared to the settings on the server and the appropriate rules
are added or deleted from the rule database in memory. When you
click Save in the Web Assistant window, the rule database is stored
in the application's `user.d2wmodel` file.

To build the Web Assistant's list of available task pages
and property-level components, Direct to Web uses the rule system
differently from when it renders a page. Instead of firing the single
best candidate rule to find a particular key, Direct to Web asks
for all rules that can resolve the key given the state of the Direct
to Web context and collects the resulting values into a list that
the Web Assistant presents to you. Two special keys are handled
this way: `pageAvailable` for
collecting task pages and `componentAvailable` for collecting
property-level components.

If you want to see which rules the Web Assistant creates and
deletes at runtime, you can run your application with the switch
`-D2WTraceRuleModificationsEnabled YES`.

### Rule Firing Cache

When a rule fires, its right-hand-side value is cached to
improve Direct to Web's rendering performance. Once the value
is cached, subsequent requests for the key may cause the rule engine
to access the cache to resolve its value instead of finding a rule
to fire. The cache is retained for the life of the application or
until you click Update, Save, or Revert in the Web Assistant.

It is important to note that the right-hand-side value is
cached based on the values of a collection of keys that does not
necessarily include all of the keys on the left-hand side of the
rule. Only the values of a list of _significant keys_ and
the right-hand-side key are used to uniquely identify the cache
entry. By default, the significant keys are

- task
- entity
- propertyKey
- configuration

The configuration key refers to the named configuration of
the current page. You can add to this list using the D2W class's `newSignificantKey` method.

Consider this rule:

```
((task = "edit") and (entity.name = "Movie")
    and (propertyKey = "studio"))
    => componentName = "D2WEditToOneRelationship"
```

When it fires, Direct to Web creates the cache entry described
in [Table 3-8](#apple-ijauurcki5bui).

__Table
3-8__

| `task` | "edit" |
| `entity` | `<EOEntity Movie>` |
| `propertyKey` | "studio" |
| `configuration` | `null` |
| `key` | `componentName` |
| `value` | "D2WEditRelationship" |

If the Direct to Web context is asked for the value of the `componentName` key
again, and the context's values for `task`, `entity`, `propertyKey`,
and `configuration` are
unchanged, this rule does not fire. Instead, the rule system uses
the cached value. On the other hand, if the value of any of these
keys changes, the cache entry no longer applies and the rule engine
must find a rule to fire to resolve the `componentName` key.

#### Caching Gotchas

If you watch the rules as they fire (with `-D2WTraceRuleFiringEnabled
YES`), you may find rules that fire when you
expect Direct to Web to use the values in the cache. Or rules you expect
to fire don't appear because Direct to Web gets the values from
the cache.

To see how a rule might fire when you expect its value to
be cached, consider the rule that resolves the `look` key,
which defines whether the application is using the Basic look, the Neutral
look, or the WebObjects look. Suppose the rule is

```
*true* => look = "NeutralLook"
```

The first time this rule fires is when the Direct to Web factory
asks for the name of the Direct to Web template to display the QueryAll
page. The following cache entry is created:

__Table 3-9__

| `task` | "queryAll" |
| `entity` | null |
| `propertyKey` | null |
| `configuration` | `null` |
| `key` | look |
| `value` | "NeutralLook" |

Note that the `entity` key
is `null`. The next time Direct to
Web asks for the `look` key
is when it wants to know the background color for the Query form
table. The entity is still `null` so Direct
to Web gets the value from the cache.

Now the QueryAll template begins to iterate through the entities.
It sets the first entity to the Movie EOEntity. This time the `entity` key
is no longer `null` so
the old cache entry does not apply. Consequently, the rule engine
fires the `look` rule again.

What is more difficult to debug is when the rule engine resolves
a key using the cache when you expect a rule to fire. This happens
when the outcome of the rule depends on a key that is not cached
(that is, not in the list of significant keys). This can arise in
an application that has different behavior depending on the user's
access privileges.

Consider an online movie database application that behaves
differently based on the user's access privileges. In particular,
the administrator (access level 1) sees the AdminListMovie template
and the customer (access level 3) sees the CustomerListMovie template.
You can set this up with these rules:

```
((task = "list") and (entity = "Movie") and (session.user.accessLevel = 1))
    => pageName = "AdminListMovie"

((task = "list") and (entity = "Movie") and (session.user.accessLevel = 3))
    => pageName = "CustomerListMovie"
```

Suppose the administrator logs into the application and accesses
the list page. Direct to Web creates this cache entry:

__Table 3-10__

| `task` | "list" |
| `entity` | <EOEntity Movie> |
| `propertyKey` | null |
| `configuration` | `null` |
| `key` | pageName |
| `value` | "AdminListMovie" |

__|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| task | entity | propertyKey | configuration | key | value |__| "list" | `<EOEntity Movie>` | `null` | `null` | `pageName` | "AdminListMovie" |

Later a customer logs on and access the list page. Instead
of showing the customer list page, Direct to Web displays the administrator's
list page, which is an obvious security violation. This happens
because the second rule never fires. Instead, the cache entry from the
first rule resolves the value for the `pageName` key.

To fix the application, you need to add `session.user.accessLevel` to
the list of significant keys using the D2W class's `newSignificantKey` method.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Resolving_K_he_Property.md)[![Next](attachments/DirectToWeb/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Customizing/index.html)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
