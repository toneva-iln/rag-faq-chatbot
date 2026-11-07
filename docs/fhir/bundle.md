# 2.36   Resource Bundle - Content 

|  |  |  |  |  |
|----|----|----|----|----|
| [FHIR Infrastructure ](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group | [Maturity Level](versions.html#maturity): [N](versions.html#std-process) |  [Normative](versions.html#std-process "Standard Status") (from v4.0.0) | [Security Category](security.html#SecPrivConsiderations): Not Classified | [Compartments](compartmentdefinition.html): Not linked to any defined compartments |

|  |  |
|----|----|
|  | This page has been approved as part of an [ANSI ](https://www.ansi.org/) standard. See the [Infrastructure](ansi-infrastructure.html) Package for further details. |

A container for a collection of resources.

## 2.36.1 Scope and Usage 

One common operation performed with resources is to gather a collection of resources into a single instance with containing context. In FHIR this is referred to as "bundling" the resources together. These resource bundles are useful for a variety of different reasons, including:

- Returning a set of resources that meet some criteria as part of a server operation (see [RESTful Search](http.html#search))
- Returning a set of versions of resources as part of the history operation on a server (see [History](http.html#history))
- Sending a set of resources as part of a message exchange (see [Messaging](messaging.html))
- Grouping a self-contained set of resources to act as an exchangeable and persistable collection with clinical integrity - e.g. a clinical document (see [Documents](documents.html))
- Creating/updating/deleting a set of resources on a server as a single operation (including doing so as a single atomic transaction) (see [Transactions](http.html#transaction))
- Storing a collection of resources

## 2.36.2 Boundaries and Relationships 

There are two ways to collect resources together for transport and persistence purposes - [contained resources](references.html#contained), and bundles. There is an important difference between the two:

- Contained resources are "in" the container resource - they can only ever be interpreted and/or changed in the context of the container
- A bundle is a collection of resources that can have an independent existence - for example, they might also be accessed directly using the [RESTful API](http.html)

In addition to these two technical mechanisms, there are three administrative and infrastructure resources which also support grouping of content. These resources do not contain resources directly, but instead use \[Reference\] to point to the grouped resources:

- The [List](list.html) resource – Enumerates a flat collection of resources and provides features for managing the collection. While a particular List instance may represent a "snapshot", from a business process perspective the notion of "List" is dynamic – items are added and removed over time. The list resource references other resources. Lists may be curated and have specific business meaning.
- The [Group](group.html) resource – Defines a group of specific people, animals, devices, etc. by enumerating them, or by describing qualities that group members have. The group resource refers to other resources, possibly implicitly. Groups are intended to be acted upon or observed as a whole; e.g. performing therapy on a group, calculating risk for a group, etc. This resource will commonly be used for public health (e.g. describing an at-risk population), clinical trials (e.g. defining a test subject pool) and similar purposes.
- The [Composition](composition.html) resource – Defines a set of healthcare-related information that is assembled together into a single logical document that provides a single coherent statement of meaning, establishes its own context and that has clinical attestation with regard to who is making the statement. The composition resource provides the basic structure of a FHIR [document](documents.html). The full content of the document is expressed using a Bundle. Compositions will often reference Lists as the focus of particular sections.

These three resources represent meaningful groupings of the resources they refer to (e.g. a discharge medication List, a Group of participants for a clinical trial, a set of resources that form a signed document), while a Bundle is merely is a container for resources used for transfer and storage. This list is not exhaustive; other resources also provde grouping functionality.

## 2.36.3 Resource Content 

- [Structure](#tabs-struc)
- [UML](#tabs-uml)
- [XML](#tabs-xml)
- [JSON](#tabs-json)
- [Turtle](#tabs-ttl)
- [R3 Diff](#tabs-diff)
- [All](#tabs-all)

**Structure**

[TABLE]

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

\
\<[**Bundle**](bundle-definitions.html#Bundle "A container for a collection of resources.") xmlns="http://hl7.org/fhir"\> [](xml.html "Documentation for this format")\
 \<!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) --\>\
 \<[**identifier**](bundle-definitions.html#Bundle.identifier "A persistent identifier for the bundle that won't change as a bundle is copied from server to server.")\>\<!-- **0..1** [Identifier](datatypes.html#Identifier) [Persistent identifier for the bundle](terminologies.html#unbound) --\>\</identifier\>\
 \<[**type**](bundle-definitions.html#Bundle.type "Indicates the purpose of this bundle - how it is intended to be used.") value="\[[code](datatypes.html#code)\]"/\>\<!-- **1..1** [document \| message \| transaction \| transaction-response \| batch \| batch-response \| history \| searchset \| collection](valueset-bundle-type.html) --\>\
 \<[**timestamp**](bundle-definitions.html#Bundle.timestamp "The date/time that the bundle was assembled - i.e. when the resources were placed in the bundle.") value="\[[instant](datatypes.html#instant)\]"/\>\<!-- **0..1** [When the bundle was assembled](terminologies.html#unbound) --\>\
 \<[**total**](bundle-definitions.html#Bundle.total "If a set of search matches, this is the total number of entries of type 'match' across all pages in the search.  It does not include search.mode = 'include' or 'outcome' entries and it does not provide a count of the number of entries in the Bundle.") value="\[[unsignedInt](datatypes.html#unsignedInt)\]"/\>\<!-- ** 0..1** [If search, the total number of matches](terminologies.html#unbound) --\>\
 \<[**link**](bundle-definitions.html#Bundle.link "A series of links that provide context to this bundle.")\>  \<!-- **0..\*** Links related to this Bundle --\>\
  \<[**relation**](bundle-definitions.html#Bundle.link.relation "A name which details the functional use for this link - see [http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1](http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1).") value="\[[string](datatypes.html#string)\]"/\>\<!-- **1..1** [See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1](terminologies.html#unbound) --\>\
  \<[**url**](bundle-definitions.html#Bundle.link.url "The reference details for the link.") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **1..1** [Reference details for the link](terminologies.html#unbound) --\>\
 \</link\>\
 \<[**entry**](bundle-definitions.html#Bundle.entry "An entry in a bundle resource - will either contain a resource or information about a resource (transactions and history only).")\>  \<!-- **0..\*** Entry in the bundle - will have a resource or information --\>\
  \<[**link**](bundle-definitions.html#Bundle.entry.link "A series of links that provide context to this entry.")\>\<!-- **0..\*** Content as for Bundle.link [Links related to this entry](terminologies.html#unbound) --\>\</link\>\
  \<[**fullUrl**](bundle-definitions.html#Bundle.entry.fullUrl "The Absolute URL for the resource.  The fullUrl SHALL NOT disagree with the id in the resource - i.e. if the fullUrl is not a urn:uuid, the URL shall be version-independent URL consistent with the Resource.id. The fullUrl is a version independent reference to the resource. The fullUrl element SHALL have a value except that: 
* fullUrl can be empty on a POST (although it does not need to when specifying a temporary id for reference in the bundle)
* Results from operations might involve resources that are not identified.") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **0..1** [URI for resource (Absolute URL server address or URI for UUID/OID)](terminologies.html#unbound) --\>\
  \<[**resource**](bundle-definitions.html#Bundle.entry.resource "The Resource for the entry. The purpose/meaning of the resource is determined by the Bundle.type.")\>\<!-- **0..1** [Resource](resource.html#Resource) [A resource in the bundle](terminologies.html#unbound) --\>\</resource\>\
  \<[**search**](bundle-definitions.html#Bundle.entry.search "Information about the search process that lead to the creation of this entry.")\>  \<!-- ** 0..1** Search related information --\>\
   \<[**mode**](bundle-definitions.html#Bundle.entry.search.mode "Why this entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.") value="\[[code](datatypes.html#code)\]"/\>\<!-- **0..1** [match \| include \| outcome - why this is in the result set](valueset-search-entry-mode.html) --\>\
   \<[**score**](bundle-definitions.html#Bundle.entry.search.score "When searching, the server's search ranking score for the entry.") value="\[[decimal](datatypes.html#decimal)\]"/\>\<!-- **0..1** [Search ranking (between 0 and 1)](terminologies.html#unbound) --\>\
  \</search\>\
  \<[**request**](bundle-definitions.html#Bundle.entry.request "Additional information about how this entry should be processed as part of a transaction or batch.  For history, it shows how the entry was processed to create the version contained in the entry.")\>  \<!-- ** 0..1** Additional execution information (transaction/batch/history) --\>\
   \<[**method**](bundle-definitions.html#Bundle.entry.request.method "In a transaction or batch, this is the HTTP action to be executed for this entry. In a history bundle, this indicates the HTTP action that occurred.") value="\[[code](datatypes.html#code)\]"/\>\<!-- **1..1** [GET \| HEAD \| POST \| PUT \| DELETE \| PATCH](valueset-http-verb.html) --\>\
   \<[**url**](bundle-definitions.html#Bundle.entry.request.url "The URL for this entry, relative to the root (the address to which the request is posted).") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **1..1** [URL for HTTP equivalent of this entry](terminologies.html#unbound) --\>\
   \<[**ifNoneMatch**](bundle-definitions.html#Bundle.entry.request.ifNoneMatch "If the ETag values match, return a 304 Not Modified status. See the API documentation for ["Conditional Read"](http.html#cread).") value="\[[string](datatypes.html#string)\]"/\>\<!-- **0..1** [For managing cache currency](terminologies.html#unbound) --\>\
   \<[**ifModifiedSince**](bundle-definitions.html#Bundle.entry.request.ifModifiedSince "Only perform the operation if the last updated date matches. See the API documentation for ["Conditional Read"](http.html#cread).") value="\[[instant](datatypes.html#instant)\]"/\>\<!-- **0..1** [For managing cache currency](terminologies.html#unbound) --\>\
   \<[**ifMatch**](bundle-definitions.html#Bundle.entry.request.ifMatch "Only perform the operation if the Etag value matches. For more information, see the API section ["Managing Resource Contention"](http.html#concurrency).") value="\[[string](datatypes.html#string)\]"/\>\<!-- **0..1** [For managing update contention](terminologies.html#unbound) --\>\
   \<[**ifNoneExist**](bundle-definitions.html#Bundle.entry.request.ifNoneExist "Instruct the server not to perform the create if a specified resource already exists. For further information, see the API documentation for ["Conditional Create"](http.html#ccreate). This is just the query portion of the URL - what follows the "?" (not including the "?").") value="\[[string](datatypes.html#string)\]"/\>\<!-- **0..1** [For conditional creates](terminologies.html#unbound) --\>\
  \</request\>\
  \<[**response**](bundle-definitions.html#Bundle.entry.response "Indicates the results of processing the corresponding 'request' entry in the batch or transaction being responded to or what the results of an operation where when returning history.")\>  \<!-- ** 0..1** Results of execution (transaction/batch/history) --\>\
   \<[**status**](bundle-definitions.html#Bundle.entry.response.status "The status code returned by processing this entry. The status SHALL start with a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description associated with the status code.") value="\[[string](datatypes.html#string)\]"/\>\<!-- **1..1** [Status response code (text optional)](terminologies.html#unbound) --\>\
   \<[**location**](bundle-definitions.html#Bundle.entry.response.location "The location header created by processing this operation, populated if the operation returns a location.") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **0..1** [The location (if the operation returns a location)](terminologies.html#unbound) --\>\
   \<[**etag**](bundle-definitions.html#Bundle.entry.response.etag "The Etag for the resource, if the operation for the entry produced a versioned resource (see [Resource Metadata and Versioning](http.html#versioning) and [Managing Resource Contention](http.html#concurrency)).") value="\[[string](datatypes.html#string)\]"/\>\<!-- **0..1** [The Etag for the resource (if relevant)](terminologies.html#unbound) --\>\
   \<[**lastModified**](bundle-definitions.html#Bundle.entry.response.lastModified "The date/time that the resource was modified on the server.") value="\[[instant](datatypes.html#instant)\]"/\>\<!-- **0..1** [Server's date time modified](terminologies.html#unbound) --\>\
   \<[**outcome**](bundle-definitions.html#Bundle.entry.response.outcome "An OperationOutcome containing hints and warnings produced as part of processing this entry in a batch or transaction.")\>\<!-- **0..1** [Resource](resource.html#Resource) [OperationOutcome with hints and warnings (for batch/transaction)](terminologies.html#unbound) --\>\</outcome\>\
  \</response\>\
 \</entry\>\
 \<[**signature**](bundle-definitions.html#Bundle.signature "Digital Signature - base64 encoded. XML-DSig or a JWT.")\>\<!-- **0..1** [Signature](datatypes.html#Signature) [Digital Signature](terminologies.html#unbound) --\>\</signature\>\
\</Bundle\>\

**JSON Template**

\
{[](json.html "Documentation for this format")\
  "resourceType" : "[**Bundle**](bundle-definitions.html#Bundle "A container for a collection of resources.")",\
  // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)\
  "[identifier](bundle-definitions.html#Bundle.identifier "A persistent identifier for the bundle that won't change as a bundle is copied from server to server.")" : { [Identifier](datatypes.html#Identifier) }, // [Persistent identifier for the bundle](terminologies.html#unbound)\
  "[type](bundle-definitions.html#Bundle.type "Indicates the purpose of this bundle - how it is intended to be used.")" : "\<[code](datatypes.html#code)\>", // **R!**  [document \| message \| transaction \| transaction-response \| batch \| batch-response \| history \| searchset \| collection](valueset-bundle-type.html)\
  "[timestamp](bundle-definitions.html#Bundle.timestamp "The date/time that the bundle was assembled - i.e. when the resources were placed in the bundle.")" : "\<[instant](datatypes.html#instant)\>", // [When the bundle was assembled](terminologies.html#unbound)\
  "[total](bundle-definitions.html#Bundle.total "If a set of search matches, this is the total number of entries of type 'match' across all pages in the search.  It does not include search.mode = 'include' or 'outcome' entries and it does not provide a count of the number of entries in the Bundle.")" : "\<[unsignedInt](datatypes.html#unsignedInt)\>", // **C?** [If search, the total number of matches](terminologies.html#unbound)\
  "[link](bundle-definitions.html#Bundle.link "A series of links that provide context to this bundle.")" : \[{ // [Links related to this Bundle](terminologies.html#unbound)\
    "[relation](bundle-definitions.html#Bundle.link.relation "A name which details the functional use for this link - see [http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1](http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1).")" : "\<[string](datatypes.html#string)\>", // **R!**  [See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1](terminologies.html#unbound)\
    "[url](bundle-definitions.html#Bundle.link.url "The reference details for the link.")" : "\<[uri](datatypes.html#uri)\>" // **R!**  [Reference details for the link](terminologies.html#unbound)\
  }\],\
  "[entry](bundle-definitions.html#Bundle.entry "An entry in a bundle resource - will either contain a resource or information about a resource (transactions and history only).")" : \[{ // [Entry in the bundle - will have a resource or information](terminologies.html#unbound)\
    "[link](bundle-definitions.html#Bundle.entry.link "A series of links that provide context to this entry.")" : \[{ Content as for Bundle.link }\], // [Links related to this entry](terminologies.html#unbound)\
    "[fullUrl](bundle-definitions.html#Bundle.entry.fullUrl "The Absolute URL for the resource.  The fullUrl SHALL NOT disagree with the id in the resource - i.e. if the fullUrl is not a urn:uuid, the URL shall be version-independent URL consistent with the Resource.id. The fullUrl is a version independent reference to the resource. The fullUrl element SHALL have a value except that: 
* fullUrl can be empty on a POST (although it does not need to when specifying a temporary id for reference in the bundle)
* Results from operations might involve resources that are not identified.")" : "\<[uri](datatypes.html#uri)\>", // [URI for resource (Absolute URL server address or URI for UUID/OID)](terminologies.html#unbound)\
    "[resource](bundle-definitions.html#Bundle.entry.resource "The Resource for the entry. The purpose/meaning of the resource is determined by the Bundle.type.")" : { [Resource](resource.html#Resource) }, // [A resource in the bundle](terminologies.html#unbound)\
    "[search](bundle-definitions.html#Bundle.entry.search "Information about the search process that lead to the creation of this entry.")" : { // **C?** [Search related information](terminologies.html#unbound)\
      "[mode](bundle-definitions.html#Bundle.entry.search.mode "Why this entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.")" : "\<[code](datatypes.html#code)\>", // [match \| include \| outcome - why this is in the result set](valueset-search-entry-mode.html)\
      "[score](bundle-definitions.html#Bundle.entry.search.score "When searching, the server's search ranking score for the entry.")" : \<[decimal](datatypes.html#decimal)\> // [Search ranking (between 0 and 1)](terminologies.html#unbound)\
    },\
    "[request](bundle-definitions.html#Bundle.entry.request "Additional information about how this entry should be processed as part of a transaction or batch.  For history, it shows how the entry was processed to create the version contained in the entry.")" : { // **C?** [Additional execution information (transaction/batch/history)](terminologies.html#unbound)\
      "[method](bundle-definitions.html#Bundle.entry.request.method "In a transaction or batch, this is the HTTP action to be executed for this entry. In a history bundle, this indicates the HTTP action that occurred.")" : "\<[code](datatypes.html#code)\>", // **R!**  [GET \| HEAD \| POST \| PUT \| DELETE \| PATCH](valueset-http-verb.html)\
      "[url](bundle-definitions.html#Bundle.entry.request.url "The URL for this entry, relative to the root (the address to which the request is posted).")" : "\<[uri](datatypes.html#uri)\>", // **R!**  [URL for HTTP equivalent of this entry](terminologies.html#unbound)\
      "[ifNoneMatch](bundle-definitions.html#Bundle.entry.request.ifNoneMatch "If the ETag values match, return a 304 Not Modified status. See the API documentation for ["Conditional Read"](http.html#cread).")" : "\<[string](datatypes.html#string)\>", // [For managing cache currency](terminologies.html#unbound)\
      "[ifModifiedSince](bundle-definitions.html#Bundle.entry.request.ifModifiedSince "Only perform the operation if the last updated date matches. See the API documentation for ["Conditional Read"](http.html#cread).")" : "\<[instant](datatypes.html#instant)\>", // [For managing cache currency](terminologies.html#unbound)\
      "[ifMatch](bundle-definitions.html#Bundle.entry.request.ifMatch "Only perform the operation if the Etag value matches. For more information, see the API section ["Managing Resource Contention"](http.html#concurrency).")" : "\<[string](datatypes.html#string)\>", // [For managing update contention](terminologies.html#unbound)\
      "[ifNoneExist](bundle-definitions.html#Bundle.entry.request.ifNoneExist "Instruct the server not to perform the create if a specified resource already exists. For further information, see the API documentation for ["Conditional Create"](http.html#ccreate). This is just the query portion of the URL - what follows the "?" (not including the "?").")" : "\<[string](datatypes.html#string)\>" // [For conditional creates](terminologies.html#unbound)\
    },\
    "[response](bundle-definitions.html#Bundle.entry.response "Indicates the results of processing the corresponding 'request' entry in the batch or transaction being responded to or what the results of an operation where when returning history.")" : { // **C?** [Results of execution (transaction/batch/history)](terminologies.html#unbound)\
      "[status](bundle-definitions.html#Bundle.entry.response.status "The status code returned by processing this entry. The status SHALL start with a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description associated with the status code.")" : "\<[string](datatypes.html#string)\>", // **R!**  [Status response code (text optional)](terminologies.html#unbound)\
      "[location](bundle-definitions.html#Bundle.entry.response.location "The location header created by processing this operation, populated if the operation returns a location.")" : "\<[uri](datatypes.html#uri)\>", // [The location (if the operation returns a location)](terminologies.html#unbound)\
      "[etag](bundle-definitions.html#Bundle.entry.response.etag "The Etag for the resource, if the operation for the entry produced a versioned resource (see [Resource Metadata and Versioning](http.html#versioning) and [Managing Resource Contention](http.html#concurrency)).")" : "\<[string](datatypes.html#string)\>", // [The Etag for the resource (if relevant)](terminologies.html#unbound)\
      "[lastModified](bundle-definitions.html#Bundle.entry.response.lastModified "The date/time that the resource was modified on the server.")" : "\<[instant](datatypes.html#instant)\>", // [Server's date time modified](terminologies.html#unbound)\
      "[outcome](bundle-definitions.html#Bundle.entry.response.outcome "An OperationOutcome containing hints and warnings produced as part of processing this entry in a batch or transaction.")" : { [Resource](resource.html#Resource) } // [OperationOutcome with hints and warnings (for batch/transaction)](terminologies.html#unbound)\
    }\
  }\],\
  "[signature](bundle-definitions.html#Bundle.signature "Digital Signature - base64 encoded. XML-DSig or a JWT.")" : { [Signature](datatypes.html#Signature) } // [Digital Signature](terminologies.html#unbound)\
}\

**Turtle Template**

\
@prefix fhir: \<http://hl7.org/fhir/\> .[](rdf.html "Documentation for this format")\
\
\
\[ a fhir:[**Bundle**](bundle-definitions.html#Bundle "A container for a collection of resources.");\
  fhir:nodeRole fhir:treeRoot; # if this is the parser root\
\
  # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)\
  fhir:[Bundle.identifier](bundle-definitions.html#Bundle.identifier "A persistent identifier for the bundle that won't change as a bundle is copied from server to server.") \[ [Identifier](datatypes.html#Identifier) \]; # 0..1 Persistent identifier for the bundle\
  fhir:[Bundle.type](bundle-definitions.html#Bundle.type "Indicates the purpose of this bundle - how it is intended to be used.") \[ [code](datatypes.html#code) \]; # 1..1 document \| message \| transaction \| transaction-response \| batch \| batch-response \| history \| searchset \| collection\
  fhir:[Bundle.timestamp](bundle-definitions.html#Bundle.timestamp "The date/time that the bundle was assembled - i.e. when the resources were placed in the bundle.") \[ [instant](datatypes.html#instant) \]; # 0..1 When the bundle was assembled\
  fhir:[Bundle.total](bundle-definitions.html#Bundle.total "If a set of search matches, this is the total number of entries of type 'match' across all pages in the search.  It does not include search.mode = 'include' or 'outcome' entries and it does not provide a count of the number of entries in the Bundle.") \[ [unsignedInt](datatypes.html#unsignedInt) \]; # 0..1 If search, the total number of matches\
  fhir:[Bundle.link](bundle-definitions.html#Bundle.link "A series of links that provide context to this bundle.") \[ # 0..\* Links related to this Bundle\
    fhir:[Bundle.link.relation](bundle-definitions.html#Bundle.link.relation "A name which details the functional use for this link - see [http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1](http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1).") \[ [string](datatypes.html#string) \]; # 1..1 See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1\
    fhir:[Bundle.link.url](bundle-definitions.html#Bundle.link.url "The reference details for the link.") \[ [uri](datatypes.html#uri) \]; # 1..1 Reference details for the link\
  \], ...;\
  fhir:[Bundle.entry](bundle-definitions.html#Bundle.entry "An entry in a bundle resource - will either contain a resource or information about a resource (transactions and history only).") \[ # 0..\* Entry in the bundle - will have a resource or information\
    fhir:[Bundle.entry.link](bundle-definitions.html#Bundle.entry.link "A series of links that provide context to this entry.") \[ [See Bundle.link](#ttl-Bundle.link) \], ... ; # 0..\* Links related to this entry\
    fhir:[Bundle.entry.fullUrl](bundle-definitions.html#Bundle.entry.fullUrl "The Absolute URL for the resource.  The fullUrl SHALL NOT disagree with the id in the resource - i.e. if the fullUrl is not a urn:uuid, the URL shall be version-independent URL consistent with the Resource.id. The fullUrl is a version independent reference to the resource. The fullUrl element SHALL have a value except that: 
* fullUrl can be empty on a POST (although it does not need to when specifying a temporary id for reference in the bundle)
* Results from operations might involve resources that are not identified.") \[ [uri](datatypes.html#uri) \]; # 0..1 URI for resource (Absolute URL server address or URI for UUID/OID)\
    fhir:[Bundle.entry.resource](bundle-definitions.html#Bundle.entry.resource "The Resource for the entry. The purpose/meaning of the resource is determined by the Bundle.type.") \[ [Resource](resource.html#Resource) \]; # 0..1 A resource in the bundle\
    fhir:[Bundle.entry.search](bundle-definitions.html#Bundle.entry.search "Information about the search process that lead to the creation of this entry.") \[ # 0..1 Search related information\
      fhir:[Bundle.entry.search.mode](bundle-definitions.html#Bundle.entry.search.mode "Why this entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.") \[ [code](datatypes.html#code) \]; # 0..1 match \| include \| outcome - why this is in the result set\
      fhir:[Bundle.entry.search.score](bundle-definitions.html#Bundle.entry.search.score "When searching, the server's search ranking score for the entry.") \[ [decimal](datatypes.html#decimal) \]; # 0..1 Search ranking (between 0 and 1)\
    \];\
    fhir:[Bundle.entry.request](bundle-definitions.html#Bundle.entry.request "Additional information about how this entry should be processed as part of a transaction or batch.  For history, it shows how the entry was processed to create the version contained in the entry.") \[ # 0..1 Additional execution information (transaction/batch/history)\
      fhir:[Bundle.entry.request.method](bundle-definitions.html#Bundle.entry.request.method "In a transaction or batch, this is the HTTP action to be executed for this entry. In a history bundle, this indicates the HTTP action that occurred.") \[ [code](datatypes.html#code) \]; # 1..1 GET \| HEAD \| POST \| PUT \| DELETE \| PATCH\
      fhir:[Bundle.entry.request.url](bundle-definitions.html#Bundle.entry.request.url "The URL for this entry, relative to the root (the address to which the request is posted).") \[ [uri](datatypes.html#uri) \]; # 1..1 URL for HTTP equivalent of this entry\
      fhir:[Bundle.entry.request.ifNoneMatch](bundle-definitions.html#Bundle.entry.request.ifNoneMatch "If the ETag values match, return a 304 Not Modified status. See the API documentation for ["Conditional Read"](http.html#cread).") \[ [string](datatypes.html#string) \]; # 0..1 For managing cache currency\
      fhir:[Bundle.entry.request.ifModifiedSince](bundle-definitions.html#Bundle.entry.request.ifModifiedSince "Only perform the operation if the last updated date matches. See the API documentation for ["Conditional Read"](http.html#cread).") \[ [instant](datatypes.html#instant) \]; # 0..1 For managing cache currency\
      fhir:[Bundle.entry.request.ifMatch](bundle-definitions.html#Bundle.entry.request.ifMatch "Only perform the operation if the Etag value matches. For more information, see the API section ["Managing Resource Contention"](http.html#concurrency).") \[ [string](datatypes.html#string) \]; # 0..1 For managing update contention\
      fhir:[Bundle.entry.request.ifNoneExist](bundle-definitions.html#Bundle.entry.request.ifNoneExist "Instruct the server not to perform the create if a specified resource already exists. For further information, see the API documentation for ["Conditional Create"](http.html#ccreate). This is just the query portion of the URL - what follows the "?" (not including the "?").") \[ [string](datatypes.html#string) \]; # 0..1 For conditional creates\
    \];\
    fhir:[Bundle.entry.response](bundle-definitions.html#Bundle.entry.response "Indicates the results of processing the corresponding 'request' entry in the batch or transaction being responded to or what the results of an operation where when returning history.") \[ # 0..1 Results of execution (transaction/batch/history)\
      fhir:[Bundle.entry.response.status](bundle-definitions.html#Bundle.entry.response.status "The status code returned by processing this entry. The status SHALL start with a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description associated with the status code.") \[ [string](datatypes.html#string) \]; # 1..1 Status response code (text optional)\
      fhir:[Bundle.entry.response.location](bundle-definitions.html#Bundle.entry.response.location "The location header created by processing this operation, populated if the operation returns a location.") \[ [uri](datatypes.html#uri) \]; # 0..1 The location (if the operation returns a location)\
      fhir:[Bundle.entry.response.etag](bundle-definitions.html#Bundle.entry.response.etag "The Etag for the resource, if the operation for the entry produced a versioned resource (see [Resource Metadata and Versioning](http.html#versioning) and [Managing Resource Contention](http.html#concurrency)).") \[ [string](datatypes.html#string) \]; # 0..1 The Etag for the resource (if relevant)\
      fhir:[Bundle.entry.response.lastModified](bundle-definitions.html#Bundle.entry.response.lastModified "The date/time that the resource was modified on the server.") \[ [instant](datatypes.html#instant) \]; # 0..1 Server's date time modified\
      fhir:[Bundle.entry.response.outcome](bundle-definitions.html#Bundle.entry.response.outcome "An OperationOutcome containing hints and warnings produced as part of processing this entry in a batch or transaction.") \[ [Resource](resource.html#Resource) \]; # 0..1 OperationOutcome with hints and warnings (for batch/transaction)\
    \];\
  \], ...;\
  fhir:[Bundle.signature](bundle-definitions.html#Bundle.signature "Digital Signature - base64 encoded. XML-DSig or a JWT.") \[ [Signature](datatypes.html#Signature) \]; # 0..1 Digital Signature\
\]\

**Changes since R3**

[TABLE]

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](bundle.diff.xml) or [JSON](bundle.diff.json).

See [R3 \<--\> R4 Conversion Maps](bundle-version-maps.html) (status = 28 tests of which 3 fail to execute. 3 fail round-trip testing and 16 r3 resources are invalid (0 errors).)

**Structure**

[TABLE]

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

\
\<[**Bundle**](bundle-definitions.html#Bundle "A container for a collection of resources.") xmlns="http://hl7.org/fhir"\> [](xml.html "Documentation for this format")\
 \<!-- from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language) --\>\
 \<[**identifier**](bundle-definitions.html#Bundle.identifier "A persistent identifier for the bundle that won't change as a bundle is copied from server to server.")\>\<!-- **0..1** [Identifier](datatypes.html#Identifier) [Persistent identifier for the bundle](terminologies.html#unbound) --\>\</identifier\>\
 \<[**type**](bundle-definitions.html#Bundle.type "Indicates the purpose of this bundle - how it is intended to be used.") value="\[[code](datatypes.html#code)\]"/\>\<!-- **1..1** [document \| message \| transaction \| transaction-response \| batch \| batch-response \| history \| searchset \| collection](valueset-bundle-type.html) --\>\
 \<[**timestamp**](bundle-definitions.html#Bundle.timestamp "The date/time that the bundle was assembled - i.e. when the resources were placed in the bundle.") value="\[[instant](datatypes.html#instant)\]"/\>\<!-- **0..1** [When the bundle was assembled](terminologies.html#unbound) --\>\
 \<[**total**](bundle-definitions.html#Bundle.total "If a set of search matches, this is the total number of entries of type 'match' across all pages in the search.  It does not include search.mode = 'include' or 'outcome' entries and it does not provide a count of the number of entries in the Bundle.") value="\[[unsignedInt](datatypes.html#unsignedInt)\]"/\>\<!-- ** 0..1** [If search, the total number of matches](terminologies.html#unbound) --\>\
 \<[**link**](bundle-definitions.html#Bundle.link "A series of links that provide context to this bundle.")\>  \<!-- **0..\*** Links related to this Bundle --\>\
  \<[**relation**](bundle-definitions.html#Bundle.link.relation "A name which details the functional use for this link - see [http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1](http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1).") value="\[[string](datatypes.html#string)\]"/\>\<!-- **1..1** [See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1](terminologies.html#unbound) --\>\
  \<[**url**](bundle-definitions.html#Bundle.link.url "The reference details for the link.") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **1..1** [Reference details for the link](terminologies.html#unbound) --\>\
 \</link\>\
 \<[**entry**](bundle-definitions.html#Bundle.entry "An entry in a bundle resource - will either contain a resource or information about a resource (transactions and history only).")\>  \<!-- **0..\*** Entry in the bundle - will have a resource or information --\>\
  \<[**link**](bundle-definitions.html#Bundle.entry.link "A series of links that provide context to this entry.")\>\<!-- **0..\*** Content as for Bundle.link [Links related to this entry](terminologies.html#unbound) --\>\</link\>\
  \<[**fullUrl**](bundle-definitions.html#Bundle.entry.fullUrl "The Absolute URL for the resource.  The fullUrl SHALL NOT disagree with the id in the resource - i.e. if the fullUrl is not a urn:uuid, the URL shall be version-independent URL consistent with the Resource.id. The fullUrl is a version independent reference to the resource. The fullUrl element SHALL have a value except that: 
* fullUrl can be empty on a POST (although it does not need to when specifying a temporary id for reference in the bundle)
* Results from operations might involve resources that are not identified.") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **0..1** [URI for resource (Absolute URL server address or URI for UUID/OID)](terminologies.html#unbound) --\>\
  \<[**resource**](bundle-definitions.html#Bundle.entry.resource "The Resource for the entry. The purpose/meaning of the resource is determined by the Bundle.type.")\>\<!-- **0..1** [Resource](resource.html#Resource) [A resource in the bundle](terminologies.html#unbound) --\>\</resource\>\
  \<[**search**](bundle-definitions.html#Bundle.entry.search "Information about the search process that lead to the creation of this entry.")\>  \<!-- ** 0..1** Search related information --\>\
   \<[**mode**](bundle-definitions.html#Bundle.entry.search.mode "Why this entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.") value="\[[code](datatypes.html#code)\]"/\>\<!-- **0..1** [match \| include \| outcome - why this is in the result set](valueset-search-entry-mode.html) --\>\
   \<[**score**](bundle-definitions.html#Bundle.entry.search.score "When searching, the server's search ranking score for the entry.") value="\[[decimal](datatypes.html#decimal)\]"/\>\<!-- **0..1** [Search ranking (between 0 and 1)](terminologies.html#unbound) --\>\
  \</search\>\
  \<[**request**](bundle-definitions.html#Bundle.entry.request "Additional information about how this entry should be processed as part of a transaction or batch.  For history, it shows how the entry was processed to create the version contained in the entry.")\>  \<!-- ** 0..1** Additional execution information (transaction/batch/history) --\>\
   \<[**method**](bundle-definitions.html#Bundle.entry.request.method "In a transaction or batch, this is the HTTP action to be executed for this entry. In a history bundle, this indicates the HTTP action that occurred.") value="\[[code](datatypes.html#code)\]"/\>\<!-- **1..1** [GET \| HEAD \| POST \| PUT \| DELETE \| PATCH](valueset-http-verb.html) --\>\
   \<[**url**](bundle-definitions.html#Bundle.entry.request.url "The URL for this entry, relative to the root (the address to which the request is posted).") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **1..1** [URL for HTTP equivalent of this entry](terminologies.html#unbound) --\>\
   \<[**ifNoneMatch**](bundle-definitions.html#Bundle.entry.request.ifNoneMatch "If the ETag values match, return a 304 Not Modified status. See the API documentation for ["Conditional Read"](http.html#cread).") value="\[[string](datatypes.html#string)\]"/\>\<!-- **0..1** [For managing cache currency](terminologies.html#unbound) --\>\
   \<[**ifModifiedSince**](bundle-definitions.html#Bundle.entry.request.ifModifiedSince "Only perform the operation if the last updated date matches. See the API documentation for ["Conditional Read"](http.html#cread).") value="\[[instant](datatypes.html#instant)\]"/\>\<!-- **0..1** [For managing cache currency](terminologies.html#unbound) --\>\
   \<[**ifMatch**](bundle-definitions.html#Bundle.entry.request.ifMatch "Only perform the operation if the Etag value matches. For more information, see the API section ["Managing Resource Contention"](http.html#concurrency).") value="\[[string](datatypes.html#string)\]"/\>\<!-- **0..1** [For managing update contention](terminologies.html#unbound) --\>\
   \<[**ifNoneExist**](bundle-definitions.html#Bundle.entry.request.ifNoneExist "Instruct the server not to perform the create if a specified resource already exists. For further information, see the API documentation for ["Conditional Create"](http.html#ccreate). This is just the query portion of the URL - what follows the "?" (not including the "?").") value="\[[string](datatypes.html#string)\]"/\>\<!-- **0..1** [For conditional creates](terminologies.html#unbound) --\>\
  \</request\>\
  \<[**response**](bundle-definitions.html#Bundle.entry.response "Indicates the results of processing the corresponding 'request' entry in the batch or transaction being responded to or what the results of an operation where when returning history.")\>  \<!-- ** 0..1** Results of execution (transaction/batch/history) --\>\
   \<[**status**](bundle-definitions.html#Bundle.entry.response.status "The status code returned by processing this entry. The status SHALL start with a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description associated with the status code.") value="\[[string](datatypes.html#string)\]"/\>\<!-- **1..1** [Status response code (text optional)](terminologies.html#unbound) --\>\
   \<[**location**](bundle-definitions.html#Bundle.entry.response.location "The location header created by processing this operation, populated if the operation returns a location.") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **0..1** [The location (if the operation returns a location)](terminologies.html#unbound) --\>\
   \<[**etag**](bundle-definitions.html#Bundle.entry.response.etag "The Etag for the resource, if the operation for the entry produced a versioned resource (see [Resource Metadata and Versioning](http.html#versioning) and [Managing Resource Contention](http.html#concurrency)).") value="\[[string](datatypes.html#string)\]"/\>\<!-- **0..1** [The Etag for the resource (if relevant)](terminologies.html#unbound) --\>\
   \<[**lastModified**](bundle-definitions.html#Bundle.entry.response.lastModified "The date/time that the resource was modified on the server.") value="\[[instant](datatypes.html#instant)\]"/\>\<!-- **0..1** [Server's date time modified](terminologies.html#unbound) --\>\
   \<[**outcome**](bundle-definitions.html#Bundle.entry.response.outcome "An OperationOutcome containing hints and warnings produced as part of processing this entry in a batch or transaction.")\>\<!-- **0..1** [Resource](resource.html#Resource) [OperationOutcome with hints and warnings (for batch/transaction)](terminologies.html#unbound) --\>\</outcome\>\
  \</response\>\
 \</entry\>\
 \<[**signature**](bundle-definitions.html#Bundle.signature "Digital Signature - base64 encoded. XML-DSig or a JWT.")\>\<!-- **0..1** [Signature](datatypes.html#Signature) [Digital Signature](terminologies.html#unbound) --\>\</signature\>\
\</Bundle\>\

**JSON Template**

\
{[](json.html "Documentation for this format")\
  "resourceType" : "[**Bundle**](bundle-definitions.html#Bundle "A container for a collection of resources.")",\
  // from [Resource](resource.html): [id](resource.html#id), [meta](resource.html#meta), [implicitRules](resource.html#implicitRules), and [language](resource.html#language)\
  "[identifier](bundle-definitions.html#Bundle.identifier "A persistent identifier for the bundle that won't change as a bundle is copied from server to server.")" : { [Identifier](datatypes.html#Identifier) }, // [Persistent identifier for the bundle](terminologies.html#unbound)\
  "[type](bundle-definitions.html#Bundle.type "Indicates the purpose of this bundle - how it is intended to be used.")" : "\<[code](datatypes.html#code)\>", // **R!**  [document \| message \| transaction \| transaction-response \| batch \| batch-response \| history \| searchset \| collection](valueset-bundle-type.html)\
  "[timestamp](bundle-definitions.html#Bundle.timestamp "The date/time that the bundle was assembled - i.e. when the resources were placed in the bundle.")" : "\<[instant](datatypes.html#instant)\>", // [When the bundle was assembled](terminologies.html#unbound)\
  "[total](bundle-definitions.html#Bundle.total "If a set of search matches, this is the total number of entries of type 'match' across all pages in the search.  It does not include search.mode = 'include' or 'outcome' entries and it does not provide a count of the number of entries in the Bundle.")" : "\<[unsignedInt](datatypes.html#unsignedInt)\>", // **C?** [If search, the total number of matches](terminologies.html#unbound)\
  "[link](bundle-definitions.html#Bundle.link "A series of links that provide context to this bundle.")" : \[{ // [Links related to this Bundle](terminologies.html#unbound)\
    "[relation](bundle-definitions.html#Bundle.link.relation "A name which details the functional use for this link - see [http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1](http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1).")" : "\<[string](datatypes.html#string)\>", // **R!**  [See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1](terminologies.html#unbound)\
    "[url](bundle-definitions.html#Bundle.link.url "The reference details for the link.")" : "\<[uri](datatypes.html#uri)\>" // **R!**  [Reference details for the link](terminologies.html#unbound)\
  }\],\
  "[entry](bundle-definitions.html#Bundle.entry "An entry in a bundle resource - will either contain a resource or information about a resource (transactions and history only).")" : \[{ // [Entry in the bundle - will have a resource or information](terminologies.html#unbound)\
    "[link](bundle-definitions.html#Bundle.entry.link "A series of links that provide context to this entry.")" : \[{ Content as for Bundle.link }\], // [Links related to this entry](terminologies.html#unbound)\
    "[fullUrl](bundle-definitions.html#Bundle.entry.fullUrl "The Absolute URL for the resource.  The fullUrl SHALL NOT disagree with the id in the resource - i.e. if the fullUrl is not a urn:uuid, the URL shall be version-independent URL consistent with the Resource.id. The fullUrl is a version independent reference to the resource. The fullUrl element SHALL have a value except that: 
* fullUrl can be empty on a POST (although it does not need to when specifying a temporary id for reference in the bundle)
* Results from operations might involve resources that are not identified.")" : "\<[uri](datatypes.html#uri)\>", // [URI for resource (Absolute URL server address or URI for UUID/OID)](terminologies.html#unbound)\
    "[resource](bundle-definitions.html#Bundle.entry.resource "The Resource for the entry. The purpose/meaning of the resource is determined by the Bundle.type.")" : { [Resource](resource.html#Resource) }, // [A resource in the bundle](terminologies.html#unbound)\
    "[search](bundle-definitions.html#Bundle.entry.search "Information about the search process that lead to the creation of this entry.")" : { // **C?** [Search related information](terminologies.html#unbound)\
      "[mode](bundle-definitions.html#Bundle.entry.search.mode "Why this entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.")" : "\<[code](datatypes.html#code)\>", // [match \| include \| outcome - why this is in the result set](valueset-search-entry-mode.html)\
      "[score](bundle-definitions.html#Bundle.entry.search.score "When searching, the server's search ranking score for the entry.")" : \<[decimal](datatypes.html#decimal)\> // [Search ranking (between 0 and 1)](terminologies.html#unbound)\
    },\
    "[request](bundle-definitions.html#Bundle.entry.request "Additional information about how this entry should be processed as part of a transaction or batch.  For history, it shows how the entry was processed to create the version contained in the entry.")" : { // **C?** [Additional execution information (transaction/batch/history)](terminologies.html#unbound)\
      "[method](bundle-definitions.html#Bundle.entry.request.method "In a transaction or batch, this is the HTTP action to be executed for this entry. In a history bundle, this indicates the HTTP action that occurred.")" : "\<[code](datatypes.html#code)\>", // **R!**  [GET \| HEAD \| POST \| PUT \| DELETE \| PATCH](valueset-http-verb.html)\
      "[url](bundle-definitions.html#Bundle.entry.request.url "The URL for this entry, relative to the root (the address to which the request is posted).")" : "\<[uri](datatypes.html#uri)\>", // **R!**  [URL for HTTP equivalent of this entry](terminologies.html#unbound)\
      "[ifNoneMatch](bundle-definitions.html#Bundle.entry.request.ifNoneMatch "If the ETag values match, return a 304 Not Modified status. See the API documentation for ["Conditional Read"](http.html#cread).")" : "\<[string](datatypes.html#string)\>", // [For managing cache currency](terminologies.html#unbound)\
      "[ifModifiedSince](bundle-definitions.html#Bundle.entry.request.ifModifiedSince "Only perform the operation if the last updated date matches. See the API documentation for ["Conditional Read"](http.html#cread).")" : "\<[instant](datatypes.html#instant)\>", // [For managing cache currency](terminologies.html#unbound)\
      "[ifMatch](bundle-definitions.html#Bundle.entry.request.ifMatch "Only perform the operation if the Etag value matches. For more information, see the API section ["Managing Resource Contention"](http.html#concurrency).")" : "\<[string](datatypes.html#string)\>", // [For managing update contention](terminologies.html#unbound)\
      "[ifNoneExist](bundle-definitions.html#Bundle.entry.request.ifNoneExist "Instruct the server not to perform the create if a specified resource already exists. For further information, see the API documentation for ["Conditional Create"](http.html#ccreate). This is just the query portion of the URL - what follows the "?" (not including the "?").")" : "\<[string](datatypes.html#string)\>" // [For conditional creates](terminologies.html#unbound)\
    },\
    "[response](bundle-definitions.html#Bundle.entry.response "Indicates the results of processing the corresponding 'request' entry in the batch or transaction being responded to or what the results of an operation where when returning history.")" : { // **C?** [Results of execution (transaction/batch/history)](terminologies.html#unbound)\
      "[status](bundle-definitions.html#Bundle.entry.response.status "The status code returned by processing this entry. The status SHALL start with a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description associated with the status code.")" : "\<[string](datatypes.html#string)\>", // **R!**  [Status response code (text optional)](terminologies.html#unbound)\
      "[location](bundle-definitions.html#Bundle.entry.response.location "The location header created by processing this operation, populated if the operation returns a location.")" : "\<[uri](datatypes.html#uri)\>", // [The location (if the operation returns a location)](terminologies.html#unbound)\
      "[etag](bundle-definitions.html#Bundle.entry.response.etag "The Etag for the resource, if the operation for the entry produced a versioned resource (see [Resource Metadata and Versioning](http.html#versioning) and [Managing Resource Contention](http.html#concurrency)).")" : "\<[string](datatypes.html#string)\>", // [The Etag for the resource (if relevant)](terminologies.html#unbound)\
      "[lastModified](bundle-definitions.html#Bundle.entry.response.lastModified "The date/time that the resource was modified on the server.")" : "\<[instant](datatypes.html#instant)\>", // [Server's date time modified](terminologies.html#unbound)\
      "[outcome](bundle-definitions.html#Bundle.entry.response.outcome "An OperationOutcome containing hints and warnings produced as part of processing this entry in a batch or transaction.")" : { [Resource](resource.html#Resource) } // [OperationOutcome with hints and warnings (for batch/transaction)](terminologies.html#unbound)\
    }\
  }\],\
  "[signature](bundle-definitions.html#Bundle.signature "Digital Signature - base64 encoded. XML-DSig or a JWT.")" : { [Signature](datatypes.html#Signature) } // [Digital Signature](terminologies.html#unbound)\
}\

**Turtle Template**

\
@prefix fhir: \<http://hl7.org/fhir/\> .[](rdf.html "Documentation for this format")\
\
\
\[ a fhir:[**Bundle**](bundle-definitions.html#Bundle "A container for a collection of resources.");\
  fhir:nodeRole fhir:treeRoot; # if this is the parser root\
\
  # from [Resource](resource.html): [.id](resource.html#id), [.meta](resource.html#meta), [.implicitRules](resource.html#implicitRules), and [.language](resource.html#language)\
  fhir:[Bundle.identifier](bundle-definitions.html#Bundle.identifier "A persistent identifier for the bundle that won't change as a bundle is copied from server to server.") \[ [Identifier](datatypes.html#Identifier) \]; # 0..1 Persistent identifier for the bundle\
  fhir:[Bundle.type](bundle-definitions.html#Bundle.type "Indicates the purpose of this bundle - how it is intended to be used.") \[ [code](datatypes.html#code) \]; # 1..1 document \| message \| transaction \| transaction-response \| batch \| batch-response \| history \| searchset \| collection\
  fhir:[Bundle.timestamp](bundle-definitions.html#Bundle.timestamp "The date/time that the bundle was assembled - i.e. when the resources were placed in the bundle.") \[ [instant](datatypes.html#instant) \]; # 0..1 When the bundle was assembled\
  fhir:[Bundle.total](bundle-definitions.html#Bundle.total "If a set of search matches, this is the total number of entries of type 'match' across all pages in the search.  It does not include search.mode = 'include' or 'outcome' entries and it does not provide a count of the number of entries in the Bundle.") \[ [unsignedInt](datatypes.html#unsignedInt) \]; # 0..1 If search, the total number of matches\
  fhir:[Bundle.link](bundle-definitions.html#Bundle.link "A series of links that provide context to this bundle.") \[ # 0..\* Links related to this Bundle\
    fhir:[Bundle.link.relation](bundle-definitions.html#Bundle.link.relation "A name which details the functional use for this link - see [http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1](http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1).") \[ [string](datatypes.html#string) \]; # 1..1 See http://www.iana.org/assignments/link-relations/link-relations.xhtml#link-relations-1\
    fhir:[Bundle.link.url](bundle-definitions.html#Bundle.link.url "The reference details for the link.") \[ [uri](datatypes.html#uri) \]; # 1..1 Reference details for the link\
  \], ...;\
  fhir:[Bundle.entry](bundle-definitions.html#Bundle.entry "An entry in a bundle resource - will either contain a resource or information about a resource (transactions and history only).") \[ # 0..\* Entry in the bundle - will have a resource or information\
    fhir:[Bundle.entry.link](bundle-definitions.html#Bundle.entry.link "A series of links that provide context to this entry.") \[ [See Bundle.link](#ttl-Bundle.link) \], ... ; # 0..\* Links related to this entry\
    fhir:[Bundle.entry.fullUrl](bundle-definitions.html#Bundle.entry.fullUrl "The Absolute URL for the resource.  The fullUrl SHALL NOT disagree with the id in the resource - i.e. if the fullUrl is not a urn:uuid, the URL shall be version-independent URL consistent with the Resource.id. The fullUrl is a version independent reference to the resource. The fullUrl element SHALL have a value except that: 
* fullUrl can be empty on a POST (although it does not need to when specifying a temporary id for reference in the bundle)
* Results from operations might involve resources that are not identified.") \[ [uri](datatypes.html#uri) \]; # 0..1 URI for resource (Absolute URL server address or URI for UUID/OID)\
    fhir:[Bundle.entry.resource](bundle-definitions.html#Bundle.entry.resource "The Resource for the entry. The purpose/meaning of the resource is determined by the Bundle.type.") \[ [Resource](resource.html#Resource) \]; # 0..1 A resource in the bundle\
    fhir:[Bundle.entry.search](bundle-definitions.html#Bundle.entry.search "Information about the search process that lead to the creation of this entry.") \[ # 0..1 Search related information\
      fhir:[Bundle.entry.search.mode](bundle-definitions.html#Bundle.entry.search.mode "Why this entry is in the result set - whether it's included as a match or because of an _include requirement, or to convey information or warning information about the search process.") \[ [code](datatypes.html#code) \]; # 0..1 match \| include \| outcome - why this is in the result set\
      fhir:[Bundle.entry.search.score](bundle-definitions.html#Bundle.entry.search.score "When searching, the server's search ranking score for the entry.") \[ [decimal](datatypes.html#decimal) \]; # 0..1 Search ranking (between 0 and 1)\
    \];\
    fhir:[Bundle.entry.request](bundle-definitions.html#Bundle.entry.request "Additional information about how this entry should be processed as part of a transaction or batch.  For history, it shows how the entry was processed to create the version contained in the entry.") \[ # 0..1 Additional execution information (transaction/batch/history)\
      fhir:[Bundle.entry.request.method](bundle-definitions.html#Bundle.entry.request.method "In a transaction or batch, this is the HTTP action to be executed for this entry. In a history bundle, this indicates the HTTP action that occurred.") \[ [code](datatypes.html#code) \]; # 1..1 GET \| HEAD \| POST \| PUT \| DELETE \| PATCH\
      fhir:[Bundle.entry.request.url](bundle-definitions.html#Bundle.entry.request.url "The URL for this entry, relative to the root (the address to which the request is posted).") \[ [uri](datatypes.html#uri) \]; # 1..1 URL for HTTP equivalent of this entry\
      fhir:[Bundle.entry.request.ifNoneMatch](bundle-definitions.html#Bundle.entry.request.ifNoneMatch "If the ETag values match, return a 304 Not Modified status. See the API documentation for ["Conditional Read"](http.html#cread).") \[ [string](datatypes.html#string) \]; # 0..1 For managing cache currency\
      fhir:[Bundle.entry.request.ifModifiedSince](bundle-definitions.html#Bundle.entry.request.ifModifiedSince "Only perform the operation if the last updated date matches. See the API documentation for ["Conditional Read"](http.html#cread).") \[ [instant](datatypes.html#instant) \]; # 0..1 For managing cache currency\
      fhir:[Bundle.entry.request.ifMatch](bundle-definitions.html#Bundle.entry.request.ifMatch "Only perform the operation if the Etag value matches. For more information, see the API section ["Managing Resource Contention"](http.html#concurrency).") \[ [string](datatypes.html#string) \]; # 0..1 For managing update contention\
      fhir:[Bundle.entry.request.ifNoneExist](bundle-definitions.html#Bundle.entry.request.ifNoneExist "Instruct the server not to perform the create if a specified resource already exists. For further information, see the API documentation for ["Conditional Create"](http.html#ccreate). This is just the query portion of the URL - what follows the "?" (not including the "?").") \[ [string](datatypes.html#string) \]; # 0..1 For conditional creates\
    \];\
    fhir:[Bundle.entry.response](bundle-definitions.html#Bundle.entry.response "Indicates the results of processing the corresponding 'request' entry in the batch or transaction being responded to or what the results of an operation where when returning history.") \[ # 0..1 Results of execution (transaction/batch/history)\
      fhir:[Bundle.entry.response.status](bundle-definitions.html#Bundle.entry.response.status "The status code returned by processing this entry. The status SHALL start with a 3 digit HTTP code (e.g. 404) and may contain the standard HTTP description associated with the status code.") \[ [string](datatypes.html#string) \]; # 1..1 Status response code (text optional)\
      fhir:[Bundle.entry.response.location](bundle-definitions.html#Bundle.entry.response.location "The location header created by processing this operation, populated if the operation returns a location.") \[ [uri](datatypes.html#uri) \]; # 0..1 The location (if the operation returns a location)\
      fhir:[Bundle.entry.response.etag](bundle-definitions.html#Bundle.entry.response.etag "The Etag for the resource, if the operation for the entry produced a versioned resource (see [Resource Metadata and Versioning](http.html#versioning) and [Managing Resource Contention](http.html#concurrency)).") \[ [string](datatypes.html#string) \]; # 0..1 The Etag for the resource (if relevant)\
      fhir:[Bundle.entry.response.lastModified](bundle-definitions.html#Bundle.entry.response.lastModified "The date/time that the resource was modified on the server.") \[ [instant](datatypes.html#instant) \]; # 0..1 Server's date time modified\
      fhir:[Bundle.entry.response.outcome](bundle-definitions.html#Bundle.entry.response.outcome "An OperationOutcome containing hints and warnings produced as part of processing this entry in a batch or transaction.") \[ [Resource](resource.html#Resource) \]; # 0..1 OperationOutcome with hints and warnings (for batch/transaction)\
    \];\
  \], ...;\
  fhir:[Bundle.signature](bundle-definitions.html#Bundle.signature "Digital Signature - base64 encoded. XML-DSig or a JWT.") \[ [Signature](datatypes.html#Signature) \]; # 0..1 Digital Signature\
\]\

**Changes since Release 3**

[TABLE]

See the [Full Difference](diff.html) for further information

This analysis is available as [XML](bundle.diff.xml) or [JSON](bundle.diff.json).

See [R3 \<--\> R4 Conversion Maps](bundle-version-maps.html) (status = 28 tests of which 3 fail to execute. 3 fail round-trip testing and 16 r3 resources are invalid (0 errors).)

 

See the [Profiles & Extensions](bundle-profiles.html) and the alternate definitions: Master Definition [XML](bundle.profile.xml.html) + [JSON](bundle.profile.json.html), [XML](xml.html) [Schema](bundle.xsd)/[Schematron](bundle.sch) + [JSON](json.html) [Schema](bundle.schema.json.html), [ShEx](bundle.shex.html) (for [Turtle](rdf.html)) & the [dependency analysis](bundle-dependencies.html)

### 2.36.3.1 Terminology Bindings 

| Path | Definition | Type | Reference |
|----|----|----|----|
| Bundle.type | Indicates the purpose of a bundle - how it is intended to be used. | [Required](terminologies.html#required) | [BundleType](valueset-bundle-type.html) |
| Bundle.entry.search.mode | Why an entry is in the result set - whether it's included as a match or because of an \_include requirement, or to convey information or warning information about the search process. | [Required](terminologies.html#required) | [SearchEntryMode](valueset-search-entry-mode.html) |
| Bundle.entry.request.method | HTTP verbs (in the HTTP command line). See \[HTTP rfc\](https://tools.ietf.org/html/rfc7231) for details. | [Required](terminologies.html#required) | [HTTPVerb](valueset-http-verb.html) |

### 2.36.3.2 Constraints 

|  |  |  |  |  |
|----|----|----|----|----|
| **id** | **Level** | **Location** | **Description** | **[Expression](fhirpath.html)** |
| **bdl-1** | [Rule](conformance-rules.html#rule) | (base) | total only when a search or history | total.empty() or (type = 'searchset') or (type = 'history') |
| **bdl-2** | [Rule](conformance-rules.html#rule) | (base) | entry.search only when a search | entry.search.empty() or (type = 'searchset') |
| **bdl-3** | [Rule](conformance-rules.html#rule) | (base) | entry.request mandatory for batch/transaction/history, otherwise prohibited | entry.all(request.exists() = (%resource.type = 'batch' or %resource.type = 'transaction' or %resource.type = 'history')) |
| **bdl-4** | [Rule](conformance-rules.html#rule) | (base) | entry.response mandatory for batch-response/transaction-response/history, otherwise prohibited | entry.all(response.exists() = (%resource.type = 'batch-response' or %resource.type = 'transaction-response' or %resource.type = 'history')) |
| **bdl-5** | [Rule](conformance-rules.html#rule) | Bundle.entry | must be a resource unless there's a request or response | resource.exists() or request.exists() or response.exists() |
| **bdl-7** | [Rule](conformance-rules.html#rule) | (base) | FullUrl must be unique in a bundle, or else entries with the same fullUrl must have different meta.versionId (except in history bundles) | (type = 'history') or entry.where(fullUrl.exists()).select(fullUrl&resource.meta.versionId).isDistinct() |
| **bdl-8** | [Rule](conformance-rules.html#rule) | Bundle.entry | fullUrl cannot be a version specific reference | fullUrl.contains('/\_history/').not() |
| **bdl-9** | [Rule](conformance-rules.html#rule) | (base) | A document must have an identifier with a system and a value | type = 'document' implies (identifier.system.exists() and identifier.value.exists()) |
| **bdl-10** | [Rule](conformance-rules.html#rule) | (base) | A document must have a date | type = 'document' implies (timestamp.hasValue()) |
| **bdl-11** | [Rule](conformance-rules.html#rule) | (base) | A document must have a Composition as the first resource | type = 'document' implies entry.first().resource.is(Composition) |
| **bdl-12** | [Rule](conformance-rules.html#rule) | (base) | A message must have a MessageHeader as the first resource | type = 'message' implies entry.first().resource.is(MessageHeader) |

### 2.36.3.3 Notes about Bundle 

- Conceptually, a bundle is a list of resources with some context (named links, and status on the entries)
- Since a Bundle is itself a [Resource](resource.html) it has the same common metadata as all resources, including profile assertions, tags, and security labels
- Although there are no extensions on the Bundle itself, `link`, `entry`, and `search`/`request`/`response` can all have extensions. See [Patient](patient.html#match) and [Location](location.html#positional) for examples on search
- Both Bundle.link and Bundle.entry.link are defined to support providing additional context when Bundles are used (e.g. [HATEOAS ](http://en.wikipedia.org/wiki/HATEOAS)). Bundle.entry.link corresponds to links found in the HTTP header if the resource in the entry was [read](http.html#read) directly. This specification defines some specific uses of Bundle.link for [searching](search.html#conformance) and [paging](http.html#paging), but no specific uses for Bundle.entry.link, and no defined function in a transaction - meaning is implementation specific
- Bundles have both .id and .identifier - see [Resource Identities](resource.html#id) for further information

### 2.36.3.4 Using Bundles 

The content and rules for using a Bundle depend on the [type](bundle-definitions.html#Bundle.type) of the bundle. Note that all bundle types use resource identity resolution as described below.

#### 2.36.3.4.1 Document 

A document Bundle (type = "document") consists of a series of entries, the first of which is a [Composition](composition.html). Each entry element SHALL contain a resource. See [Documents](documents.html) for further information.

[Example](document-example-dischargesummary.html)

#### 2.36.3.4.2 Message 

A message Bundle (type = "message") consists of a series of entries, the first of which is a [MessageHeader](messageheader.html). Each entry element SHALL contain a resource. See [Messaging](messaging.html) for further information.

Example [Request](message-request-link.html) and [Response](message-response-link.html)

#### 2.36.3.4.3 Search Results 

A set of search results (type = "searchset") consists of a series of 0 or more entries. Each entry element SHALL contain a resource. See [Search](http.html#search) for further information.

In addition, [Bundle.total](bundle-definitions.html#Bundle.total) may be used to return the total number of resources that match the search, and that may be returned by following the "next" [link](bundle-definitions.html#Bundle.link).

For each entry, a search set can also contain two specific pieces of search related information:

- [search.mode](bundle-definitions.html#Bundle.entry.search.mode): An indication of whether the resource is in the search set because it matched the search criteria or whether it is included because another resource refers to it (e.g. by the [\_include](search.html#include) parameter)
- [search.score](bundle-definitions.html#Bundle.entry.search.score): The server's search ranking score for the entry. Servers are not required to return a ranking score, but if they do, 1 is most relevant, and 0 is least relevant. Note: often, search results are sorted by score, but the client may specify a different sort order (see [Search Relevance](search.html#score))

[Example](bundle-example.html)

#### 2.36.3.4.4 History 

A change history (type = "history") consists of a series of 0 or more entries. Each entry element SHALL contain a request element that describes the change that was made and, if the method is a POST or PUT, a resource that represents the state of the resource at the conclusion of the operation. A response element SHALL also be present so that consumers can access the `location` header. See [History](http.html#history) for further information.

In addition, [Bundle.total](bundle-definitions.html#Bundle.total) may be used to return the total number of resources that are included in the change history, including those that may be returned by following the "next" [link](bundle-definitions.html#Bundle.link).

#### 2.36.3.4.5 Transaction / Batch 

A transaction (type = "transaction") or batch (type = "batch") consists of a series of 0 or more entries. Each entry element SHALL contain a request element has the details of an HTTP operation that informs the system processing the transaction what to do with the entry. If the entry method is a 'PUT' or 'POST', then the entry SHALL contain a resource that becomes the body of the HTTP operation. See [Transactions](http.html#transaction) for further information.

[Example](bundle-transaction.html)

#### 2.36.3.4.6 Transaction/Batch Response 

A transaction response (type = "transaction-response") or batch response (type="batch-response") consists of a series of 0 or more entries: 1 for each entry in the transaction or batch it is in response to. Each entry element SHALL contain a `response` element which indicates the outcome of the HTTP operation that the server performed for the entry.

[Example](bundle-response.html)

#### 2.36.3.4.7 Collection 

A collection (type = "collection") consists of a series of 0 or more entries. No particular use with respect to the FHIR specification is associated with this Bundle. Each entry element SHALL contain a resource.

[Example](diagnosticreport-examples.html)

## 2.36.4 Resource URL & Uniqueness rules in a bundle 

Except for transactions and batches, each entry in a `Bundle` must have a `fullUrl` which is the identity of the resource in the entry. Note that this is not a versioned reference to the resource, but its identity. Where a resource is not assigned a persistent identity that can be used in the Bundle, a UUID should be used (urn:uuid:...).

For transactions and batches, entries MAY not have fullURLs when the entry.request.method = POST, and the resource has no identity. Note that even in this case, there may still be a fullURL in a transaction on a POST so that relationships between resources can be represented (see [Transactions](http.html#transaction)).

A given version of a resource SHALL only appear once in each Bundle. There might, however, be multiple versions of a single resource present in a single bundle. This would be expected in Bundles of type `history`, and also might be necessitated by closely tracking Provenance.

Note that the meaning of an unversioned reference to a resource that appears multiple times is potentially ambiguous, though processors may have additional informaton to help resolve this (e.g. change order in a history bundle).

When processing batches and transactions, it is at server discretion how to behave if multiple versions of a single resource are present.

### 2.36.4.1 Resolving references in Bundles 

The `Bundle` resource is a packaging construct that has one of more entries that are other kinds of resources. Those resources themselves have references to other resources - e.g. an Observation that refers to a Patient. The referenced resources may also be found in the Bundle. For example, the system that constructed the Bundle may have included both the Observation and the Patient. The content of the references between resources doesn't change because of the bundle.

This section documents a method that resolves references correctly within a bundle. Note that this method does not define any new semantics; resolution is based on the way resource identity and resource references work.

Applications reading a Bundle should always [look for a resource](references.html#bundle-refs) by its identity in the bundle first before trying to access it by its URL externally.

How to resolve a reference in a Bundle:

- If the reference is not an absolute reference, convert it to an absolute URL:
  - if the reference has the format \[type\]/\[id\], and
  - if the fullUrl for the bundle entry containing the resource is a RESTful one (see the [RESTful URL regex](references.html#regex))
    - extract the \[root\] from the fullUrl, and append the reference (type/id) to it
    - then try to resolve within the bundle as for a RESTful URL reference.
    - If no resolution is possible, then the reference has no defined meaning within this specification
  - else no resolution is possible and the reference has no defined meaning within this specification
- else
  - Look for an entry with a fullUrl that matches the URI in the reference
  - if no match is found, and the URI is a URL that can be resolved (e.g. if an http: URL), try accessing it directly)

Note, in addition, that a reference may be by identifier, and if it is, and there is no URL, it may be resolved by scanning the ids in the bundle. Note also that transactions may contain [conditional references](http.html#trules) that must be resolved by the server before processing the matches.

If the reference is version specific (either relative or absolute), then remove the version from the URL before matching fullUrl, and then match the version based on `Resource.meta.versionId`. Note that the rules for resolving references in contained resources are the same as those for resolving resources in the resource that contains the contained resource.

If multiple matches are found, it is ambiguous which is correct. Applications MAY return an error or take some other action as they deem appropriate.

There is an [example Bundle that demonstrates](bundle-references.html) these rules.

### 2.36.4.2 Serving Bundles using the RESTful API 

The Bundle resource type has an end-point like all most other resources. This end-point serves the [usual interactions](http.html#interactions). Bundles are treated as static resources on the /Bundle end-point (i.e. when a batch, transaction, or message is POSTed to /Bundle, it is stored as is, and the content is not processed as batch, transaction, or message - instead, they are processed like normal resource, with indexing / auditing etc. Performing a GET /Bundle/\[location\] will return the same resource.

The Bundle end point does have two special search parameters - `composition` and `message`, which allow for chained search into the first (special) entries in document and message resources.

## 2.36.5 Search Parameters 

Search parameters for this resource. The [common parameters](search.html#all) also apply. See [Searching](search.html) for more information about searching in REST, messaging, and services.

[TABLE]

®© HL7.org 2011+. FHIR Release 4 (Technical Correction \#1) (v4.0.1) generated on Fri, Nov 1, 2019 09:34+1100. [QA Page](qa.html)\
Links: [Search ](http://hl7.org/fhir/search.cfm) \| [Version History](history.html) \| [Table of Contents](toc.html) \| [Credits](credits.html) \| [Compare to R3 ](https://www.fhir.org/perl/htmldiff.pl?oldfile=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fbundle.html&newfile=http%3A%2F%2Fhl7.org%2Ffhir%2FR4%2Fbundle.html) \| [](license.html) \| [Propose a change ](http://hl7.org/fhir-issues)
