---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWebRef/Java/Classes/Assignment.html
archived_at: '2026-07-15T08:12:42.597170Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/DirectToWebRef/Java/images/up.gif)](../DirectToWebTOC.md)

__Assignment__

__Package__:
com.webobjects.directtoweb

__Inherits from__:java.lang.Object__Subclasses__:

- [TabDictionaryComputer](TabDictionaryComputer.md)
- [BooleanAssignment](BooleanAssignment.md)
- [DefaultAssignment](DefaultAssignment.md)

---

__Class Description__

---

This class performs assignments on the right-hand side of rules. Every rule in the rule database has an instance of this class that holds the right-hand-side key and the right-hand-side value. The rule engine uses this class; you should never need to use it.

If you need custom assignment behavior you can subclass Assignment. To do so, you need to provide the two constructors:

`Assignment (String keyPath, Object value)
Assignment (EOKeyValueUnarchiver unarchiver)`

You can invoke `super` for each.

You can then override the `fire` method to provide the value. For example, if you define a method `myMethod` that returns the right-hand-side value `myValue` for a key, the `fire` method could look like:

```
public Object fire(D2WContext context)
{
  if (value().equals("myValue")) return myMethod(context);
}
```

__Method Types__

---

Constructors

- [public Assignment(String keyPath, Object value)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuwo3tnmvxhil2bonzwsz3onvsw45bpifzxg2lhnzwwk3tuf4ufg5dsnfxgolcpmjvgky3ufe)
- [Assignment()](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuwo3tnmvxhil2bonzwsz3onvsw45bpifzxg2lhnzwwk3tuf4ucs)
- [public Assignment(EOKeyValueUnarchiver unarchiver)](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuwo3tnmvxhil2bonzwsz3onvsw45bpifzxg2lhnzwwk3tuf4uekt2lmv4vmylmovsvk3tbojrwq2lwmvzcs)

---

Static Constants

- [keyPathKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2lhnzwwk3tuf5vwk6kqmf2gqs3fpe)
- [valueKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3ddn5xhg5bpifzxg2lhnzwwk3tuf53gc3dvmvfwk6i)

---

Assignment Parameters

- [keyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuwo3tnmvxhil3lmv4vaylunaxvg5dsnfxgolzife)
- [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuwo3tnmvxhil3un5jxi4tjnzts6u3uojuw4zzpfauq)
- [value](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuwo3tnmvxhil3wmfwhkzjpj5rguzldoqxsqrbsk5bw63tumv4hiki)

Firing the Rule

- [fire](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuwo3tnmvxhil3gnfzgkl2pmjvgky3uf4ueimsxinxw45dfpb2cs)

Private Methods

- [encodeWithKeyValueArchiver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6qltonuwo3tnmvxhil3fnzrw6zdfk5uxi2clmv4vmylmovsuc4tdnbuxmzlsf5hwe2tfmn2c6kcfj5fwk6kwmfwhkzkbojrwq2lwmvzcs)

---

__Constructors__

---

__Assignment__

public Assignment(String keyPath, Object value)

Creates an Assignment object and sets its key path and value.

---

__Assignment__

Assignment()

Standard Java no-argument constructor.

---

__Assignment__

public Assignment(EOKeyValueUnarchiver unarchiver)

Creates a DefaultAssignment object based on a EOKeyValueUnarchiver object. This constructor is used to read the assignment information from a rule file.

---

__Static Constants__

---

__keyPathKey__
java.lang.String

This constant is intentionally undocumented.

---

__valueKey__
java.lang.String

This constant is intentionally undocumented.

---

__Methods__

__encodeWithKeyValueArchiver__

public Object encodeWithKeyValueArchiver(EOKeyValueArchiver archiver)

This method is intentionally undocumented. You should never have to invoke or customize it.

---

__fire__

public Object fire(D2WContext context)

This method is invoked when a rule fires. It returns the right-hand-side value (an Object) for a right-hand-side key in the `context` Direct to Web context.

You can override this method to provide your own assignments.

---

__keyPath__

public String keyPath()

Returns the receiver's right-hand-side key.

---

__toString__

public String toString()

Returns a String that represents the assignment. This method is invoked when the `D2WTraceRuleFiringEnabled` user default is set to `YES`.

---

__value__

public Object value(D2WContext context)

Returns the receiver's right-hand-side value.

---

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
