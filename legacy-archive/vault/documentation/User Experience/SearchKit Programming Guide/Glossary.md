---
title: SearchKit Programming Guide
apple_id: TP40001071
resource_type: Guide
platform: macOS
topic: User Experience
technology: CoreServices
published: '2005-12-06'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SearchKitConcepts/searchKit_glossary/searchKit_glossary.html
archived_at: '2026-07-18T02:12:49.292968Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [SearchKit Programming Guide](Introduction.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __AIAT__

  See [Apple Information Access Toolkit (AIAT)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecsskivbuqqi).

- __Apple Information Access Toolkit (AIAT)__

  In Classic Mac OS, an object-oriented information access engine that contained a collection of tools for indexing, searching, and analyzing large volumes of documents. Search Kit is the OS X implementation of the AIAT. AIAT was formerly known by its code name V-Twin.

- __Boolean searching__

  Matching of a query string to indexed terms using Boolean (logical) operators such as `AND` and `OR` between query terms, optionally employing grouping for precedence using parentheses. The entire query expression is matched. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomi).

- __compact__

  To make an index smaller by removing unused bits. Over time, as documents get added to and removed from an index, the index’s disk or memory footprint may grow due to fragmentation. Search Kit includes APIs to check for fragmentation and to compact an index. See also [fragmentation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecssiincuuqi).

- __corpora__

  Plural form of [corpus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvooa).

- __corpus__

  A collection of one or more documents, typically related, and available to an information retrieval system. Plural: corpora.

- __document__

  In general, a specifically locatable information object of useful granularity and arbitrary structure. In Search Kit, anything that contains text and that the Search Kit client application addresses as a document—an RTF document, a PDF file, a Mail message, an Address Book entry, the contents at an Internet URL, the result of a database query, and so on. See also [document URL object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecssjiveuisa).

- __document collection__

  See [corpus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvooa).

- __document object hierarchy__

  A collection of documents in which each document exists at a location relative to a root document. The locations may may be real, as in a file system, or virtual.

- __document URL object__

  A URL to a document. In Search Kit, a document URL object comprises a scheme, a parent document URL object, and a name, with the format of each component defined by the client application. Search Kit document URL objects may be converted to or from CFURL objects. See also [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecssijbfecsa), [parent document URL object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbuuqsjizcuorq), [scheme](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecssdifcugqi).

- __fragmentation__

  In Search Kit, an unwanted increase in index size due to accumulation of unused capacity. Over time, as documents get added to and removed from an index, the index may become fragmented—its constituent documents and terms may become arranged in a manner that includes a significant amount of unused disk or memory space. See also [compact](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecsskizcemsq).

- __inclusion/exclusion result__

  See [inclusion/exclusion searching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqshijdegrq).

- __inclusion/exclusion searching__

  Unranked searching where the result simply includes documents that match the query and excludes documents that don’t. Inclusion/exclusion searches tend to be faster than ranked searches. Search Kit supports inclusion/exclusion searches. See also [relevance-based result](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsjjbeugsq).

- __index__

  A memory- or file-based sequential collection of the terms in one or more documents. In addition to terms, Search Kit indexes contain context information that specifies which documents each term belongs to, along with term and document metadata useful during display of search results. Search Kit performs its searching and analysis on indexes. See also [inverted index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsfi5eegsi); [inverted-vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqskivauqqy); [vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsei5demsa)

- __index group__

  A short-lived collection of one or more indexes; the target of a search. An index group corresponds to one or more aspects of the corpus of documents you want to search. For example, one index in a group might contain document titles, while another contains the body text of those same documents. An index group can also comprise indexes of multiple corpora. See also [corpus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvooa); [document](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecssijbfecsa).

- __information retrieval (IR)__

  The process of locating information based on a well-defined information need. An information retrieval system consists of a corpus, one or more indexes of its content, a query interface, a search system, and a results interface. See also [corpus](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvooa); [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomi).

- __inverted index__

  An index containing terms, as keys, mapped to references to the documents they appear in. The index is sorted by its keys. “Inverted” means that the documents are found by matching on terms, rather than the other way around. See also [index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsijfeecqi); [inverted-vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqskivauqqy); [vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsei5demsa)

- __inverted-vector index__

  An index containing terms mapped to document URL objects representing the documents that the terms appear in, as well as document URL objects mapped to the terms that each document contains. See also [index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsijfeecqi); [inverted index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsfi5eegsi); [vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsei5demsa).

- __IR__

  See [information retrieval (IR)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvony).

- __MIME type hint__

  Advisory metainformation suggesting the likely content type for a URL. MIME is an acronym for Multipurpose Internet Mail Extensions. In Search Kit, common MIME type hints include `text/plain`, `text/rtf`, `text/html`, `text/pdf`, and `application/msword`.

- __minimum term frequency__

  The fewest number of times a term can appear in a document and still be indexed. This functionality is not currently supported by Search Kit indexes.

- __minimum term length__

  The shortest-length term to index. When Search Kit adds terms from a document to an index, it skips over words whose length is shorter than the minimum term length.

- __name__

  In Search Kit, a document name as represented in a document URL object. For documents that are on-disk files, the name should correspond to the actual filename. For other types of documents, your application can assign any name to a document. See also [document URL object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecssjiveuisa)

- __operator__

  A character or word that has a special meaning when used in a query. Operators in Search Kit include `AND`, `OR`, `NOT`, parentheses, quotation marks, and several others. Search Kit interprets operators and determines the user's intended search type according to the operators' meanings.

- __parent document URL object__

  In Search Kit, for file-based documents, the location of the enclosing folder for a document or for another parent document URL object. Search Kit manages documents using parent-child relationships, not paths. You can construct the path of any document by following its parent document links. See also [document URL object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecssjiveuisa).

- __partial string searching__

  Matching of the terms in a query string to indexed terms, with implied wildcard characters at the start and end of each query term. Each term is matched separately. Search Kit does not currently support partial string searching as an option, but a client application can provide it by adding wildcard operators (asterisks) around each term before handing a query off to Search Kit. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomi).

- __phrase searching__

  Matching of a query string to indexed terms, with the query string considered as a complete phrase. A match occurs when the exact query phrase appears in a document. Search Kit supports phrase searching in inverted and inverted-vector indexes. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomi).

- __prefix searching__

  A specialized type of substring search. A prefix search involves matching of a term in a query string to indexed terms, with an explicit wildcard character at the end of the query term. A match occurs when the characters in the query term (minus the wildcard character) match the beginning of an indexed term. For example, the query string `car*` will match `car`, `carpet`, and `carnivore`. Search Kit supports prefix searching in inverted and inverted-vector indexes. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomi); [substring searching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvonq); [wildcard character](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomq).

- __query__

  (n.) A text string, containing terms and operators, that represents a user's information retrieval request. Various types of query supported by Search Kit include simple, prefix/suffix/substring, Boolean, phrase, and similarity. (v.) To invoke a request for information in an information retrieval system. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomi).

- __ranked searching__

  See [relevance-based result](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsjjbeugsq).

- __relevance-based result__

  See also [relevance-based search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvooi).

- __relevance-based search__

  A ranked search whose result includes a relevance rating for each document matching a query. In general, relevance ratings may be normalized to 100%, or nonnormalized. Search Kit supports only nonnormalized results. See also [inclusion/exclusion searching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqshijdegrq); [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomi).

- __root word__

  See [stem](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvoni).

- __scheme__

  A way to access a file-system or Internet resource, corresponding to an access protocol. Examples include `http`, `ftp`, and `file`. See also [document URL object](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecssjiveuisa).

- __search__

  In an information retrieval system, a process that attempts to locate documents that match a query, and that may assign relevance scores to the found documents. Upon a successful match, a search system returns references to the found documents. Search Kit supports a variety of search types, some of which can be combined. These types are simple, Boolean, ranked, unranked, phrase, similarity, prefix, suffix, and substring.

- __search object__

  In Search Kit, an opaque data type representing an asynchronous search and containing its results, accumulated as they are found. A search object is of type `SKSearchRef`.

- __similarity searching__

  Matching of a query string, typically consisting of a representative portion of a document, to indexed documents. A match occurs when Search Kit determines significant content similarity between the query and an indexed document. Search Kit supports similarity searching in vector and inverted-vector indexes. Similarity searching also works in inverted indexes in Search Kit, but performance is worse. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomi).

- __simple search__

  Matching of the terms in a query string to indexed terms using exact, character-for-character matching. Each term is matched separately. In Search Kit, by default, spaces between terms behave like Boolean `AND` operators. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomi).

- __stem__

  The root of a family of morphological or inflectional variants of a word. For example, "swim" is the stem of "swimmer," "swimming," and "swam."

- __stemming__

  The algorithm-based removal of morphological and inflectional word components, typically endings. Language dependent. Stemming is sometimes referred to as suffix stripping, although some stemming algorithms perform prefix stripping as well. IR systems use stemming to improve search quality and to reduce index size. Search Kit does not support stemming; if needed, client applications implement it. Some stemming algorithms handle only regular variants, such as converting "swimming" to "swim," and do not handle irregular variants, such as converting "swam" to "swim."

- __stopword__

  A word not to index. When Search Kit adds terms from a document to an index, it skips over words in its top-word list.

- __substring searching__

  Matching of a term in a query string to indexed terms, with explicit wildcard characters at the start and end of the query term. A match occurs when the characters in the query term (minus the wildcard characters) match the beginning, ending, or middle of an indexed term. For example, the query string `*cat*` will match `cat`, `concatenate`, `tomcat`, and `cattle`. Search Kit supports substring searching in inverted and inverted-vector indexes. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomi).

- __suffix searching__

  A specialized type of substring search. A suffix search involves matching of a term in a query string to indexed terms, with an explicit wildcard character at the start of the query term. A match occurs when the characters in the query term (minus the wildcard character) match the ending of an indexed term. For example, the query string `*ion` will match `ion`, `lion`, and `version`. Search Kit supports suffix searching in inverted and inverted-vector indexes. See also [search](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomi); [wildcard character](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomq).

- __suffix stripping__

  See [stemming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsei5deoqq).

- __summarization object__

  In Search Kit, an opaque data type representing summarization information, including the summary text. A summarization object is of type `SKSummaryRef`.

- __synonym__

  A term that an IR system considers to be equivalent to another term for both indexing and querying. For example, an IR system could define "car," "passenger vehicle," and "automobile" to be synonyms. See also [information retrieval (IR)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvony); [index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsijfeecqi); [query](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvona).

- __term__

  An atomic entry in a Search Kit index, typically corresponding to a word found in one of the index’s documents.

- __text extraction__

  Selective copying of terms from one or more documents into an index. See also [stemming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsei5deoqq); [stopword](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsjjfeesra).

- __unranked searching__

  See [inclusion/exclusion searching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqshijdegrq).

- __URL__

  Uniform Resource Locator. An Internet address, or a file-system path when formatted as a URL with a scheme. See also [scheme](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecssdifcugqi).

- __V-Twin__

  See [Apple Information Access Toolkit (AIAT)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecsskivbuqqi).

- __vector index__

  An index containing document URL objects, as keys, mapped to the terms that each document contains. See also [index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsijfeecqi); [inverted index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqsfi5eegsi); [inverted-vector index](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvbecqskivauqqy)

- __wildcard character__

  An operator used in a query that indicates matching on any character. In Search Kit, the wildcard character is the asterisk. Depending on usage, the wildcard character can indicate prefix, suffix, or substring searching. See also [operator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvomy); [query](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnbvfvjvona).

[Previous](Document%20Revision%20History.md)

