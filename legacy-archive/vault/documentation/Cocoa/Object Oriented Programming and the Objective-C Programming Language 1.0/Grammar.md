---
title: Object Oriented Programming and the Objective-C Programming Language 1.0
apple_id: TP40005191
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OOPandObjC1/Articles/ocGrammar.html
archived_at: '2026-07-15T07:17:21.882521Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Object Oriented Programming and the Objective-C Programming Language 1.0](Introduction%20to%20The%20Objective-C%20Programming%20Language%201.0.md)


[Next](Glossary.md)[Previous](Language%20Summary.md)

# Grammar

This appendix presents a formal grammar for the Objective-C extensions to the C language—as the Objective-C language is implemented for the Cocoa development environment. It adds to the grammar for ANSI standard C found in Appendix A of _The C Programming Language_ (second edition, 1988) by Brian W. Kernighan and Dennis M. Ritchie, published by Prentice Hall, and should be read in conjunction with that book.

The Objective-C extensions introduce some new symbols (such as _class interface_), but also make use of symbols (such as _function definition_) that are explained in the standard C grammar. The symbols mentioned but not explained here are listed below:

- _compound-statement_
- _constant_
- _declaration_
- _declaration-list_
- _enum-specifier_
- _expression_
- _function-definition_
- _identifier_
- _parameter-type-list_
- _string_
- _struct-declaration-list_
- _struct-or-union_
- _typedef-name_
- _type-name_

Of these, _identifier_ and _string_ are undefined terminal symbols. Objective-C adds no undefined terminal symbols of its own.

Two notational conventions used here differ from those used in _The C Programming Language_:

- Literal symbols are shown in `code font`.
- Brackets enclose optional elements.

Otherwise, this appendix attempts to follow the conventions of _The C Programming Language_. Each part of the grammar consists of a symbol and a colon in _bold_ and a list of mutually-exclusive possibilities for expanding the symbol. For example:

- _receiver:_
- _expression_
- _class-name_
- `super`

However, there is an exception: Even though they’re not mutually exclusive, the constituents of classes, categories, protocols, and blocks are listed on separate lines to clearly show the ordering of elements. For example:

- _protocol-declaration:_
- `@protocol` _protocol-name_
- [ _protocol-reference-list_ ]
- [ _interface-declaration-list_ ]
- `@end`

This exception to the general rule is easily recognized since each list terminates with `@end` or the symbol name ends with “-block”.

There are six entry points where the Objective-C language modifies the rules defined for standard C:

- External declarations
- Type specifiers
- Type qualifiers
- Primary expressions
- Exceptions
- Synchronization

This appendix is therefore divided into six sections corresponding to these points. Where a rule in the standard C grammar is modified by an Objective-C extension, the entire rule is repeated in its modified form.

- _external-declaration:_
- _function-definition_
- _declaration_
- _class-interface_
- _class-implementation_
- _category-interface_
- _category-implementation_
- _protocol-declaration_
- _protocol-declaration-list_
- _class-declaration-list_
- _class-interface:_
- `@interface`_class-name_ [ `:` _superclass-name_ ]
- [ _protocol-reference-list_ ]
- [ _instance-variables_ ]
- [ _interface-declaration-list_ ]
- `@end`
- _class-implementation:_
- `@implementation` _class-name_ [ `:` _superclass-name_ ]
- [ _implementation-definition-list_ ]
- `@end`
- _category-interface:_
- `@interface` _class-name_ `(` _category-name_ `)`
- [ _protocol-reference-list_ ]
- [ _interface-declaration-list_ ]
- `@end`
- _category-implementation:_
- `@implementation` _class-name_ `(` _category-name_ `)`
- [ _implementation-definition-list_ ]
- `@end`
- _protocol-declaration:_
- `@protocol` _protocol-name_
- [ _protocol-reference-list_ ]
- [ _interface-declaration-list_ ]
- `@end`
- _protocol-declaration-list:_
- `@protocol` _protocol-list_ `;`
- _class-declaration-list:_
- `@class` _class-list_ `;`
- _class-list:_
- _class-name_
- _class-list_`,` _class-name_
- _protocol-reference-list:_
- `<` _protocol-list_ `>`
- _protocol-list:_
- _protocol-name_
- _protocol-list_`,` _protocol-name_
- _class-name:_
- _identifier_
- _superclass-name:_
- _identifier_
- _category-name:_
- _identifier_
- _protocol-name:_
- _identifier_
- _instance-variables:_
- `{` _instance-variable-declaration_ `}`
- _instance-variable-declaration:_
- _visibility-specification_
- _struct-declaration-list_ _instance-variables_
- _instance-variable-declaration_  _visibility-specification_
- _instance-variable-declaration_  _struct-declaration-list_ _instance-variables_
- _visibility-specification:_
- `@private`
- `@protected`
- `@public`
- _interface-declaration-list:_
- _declaration_
- _method-declaration_
- _interface-declaration-list_ _declaration_
- _interface-declaration-list_ _method-declaration_
- _method-declaration:_
- _class-method-declaration_
- _instance-method-declaration_
- _class-method-declaration:_
- `+` [ _method-type_ ] _method-selector_`;`
- _instance-method-declaration:_
- `–` [ _method-type_ ] _method-selector_`;`
- _implementation-definition-list:_
- _function-definition_
- _declaration_
- _method-definition_
- _implementation-definition-list_ _function-definition_
- _implementation-definition-list_ _declaration_
- _implementation-definition-list_ _method-definition_
- _method-definition:_
- _class-method-definition_
- _instance-method-definition_
- _class-method-definition:_
- `+` [ _method-type_ ] _method-selector_ [ _declaration-list_ ] _compound-statement_
- _instance-method-definition:_
- `–` [ _method-type_ ] _method-selector_ [ _declaration-list_ ] _compound-statement_
- _method-selector:_
- _unary-selector_
- _keyword-selector_ [ `,` `...` ]
- _keyword-selector_ [ `,` _parameter-type-list_ ]
- _unary-selector:_
- _selector_
- _keyword-selector:_
- _keyword-declarator_
- _keyword-selector_ _keyword-declarator_
- _keyword-declarator:_
- `:` [ _method-type_ ] _identifier_
- _selector_`:` [ [method-type] _method-type_ ] _identifier_
- _selector:_
- _identifier_
- _method-type:_
- `(` _type-name_ `)`

- _type-specifier:_
- `void`
- `char`
- `short`
- `int`
- `long`
- `float`
- `double`
- `signed`
- `unsigned`
- `id` [ _protocol-reference-list_ ]
- _class-name_ [ _protocol-reference-list_ ]
- _struct-or-union-specifier_
- _enum-specifier_
- _typedef-name_
- _struct-or-union-specifier:_
- _struct-or-union_ [ _identifier_ ] `{` _struct-declaration-list_ `}`
- _struct-or-union_ [ _identifier_ ] `{ @defs (` _class-name_ `) }`
- _struct-or-union_ _identifier_

- _type-qualifier:_
- `const`
- `volatile`
- _protocol-qualifier_
- _protocol-qualifier:_
- `in`
- `out`
- `inout`
- `bycopy`
- `byref`
- `oneway`

- _primary-expression:_
- _identifier_
- _constant_
- _string_
- `(` _expression_ `)`
- `self`
- _message-expression_
- _selector-expression_
- _protocol-expression_
- _encode-expression_
- _message-expression:_
- [ _receiver_ _message-selector_ ]
- _receiver:_
- _expression_
- _class-name_
- `super`
- _message-selector:_
- _selector_
- _keyword-argument-list_
- _keyword-argument-list:_
- _keyword-argument_
- _keyword-argument-list_ _keyword-argument_
- _keyword-argument:_
- _selector_ `:` _expression_
- `:` _expression_
- _selector-expression:_
- `@selector (` _selector-name_ `)`
- _selector-name:_
- _selector_
- _keyword-name-list_
- _keyword-name-list:_
- _keyword-name_
- _keyword-name-list_ _keyword-name_
- _keyword-name:_
- _selector_`:`
- `:`
- _protocol-expression:_
- `@protocol (` _protocol-name_ `)`
- _encode-expression:_
- `@encode (` _type-name_ `)`

- _exception-declarator:_
- _declarator_
- _try-statement:_
- `@try`_statement_
- _catch-statement:_
- `@catch (`_exception-declarator_`)`_statement_
- _finally-statement:_
- `@finally`_statement_
- _throw-statement:_
- `@throw (`_identifier_`)`
- _try-block:_
- _try-statement_
- _catch-statement_
- [ _finally-statement_ ]

- _synchronized-statement:_
- `@synchronized (` _identifier_ `)` _statement_

[Next](Glossary.md)[Previous](Language%20Summary.md)

