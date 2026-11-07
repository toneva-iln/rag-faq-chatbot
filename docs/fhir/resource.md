# 2.26   Base Resource Definitions 

|  |  |  |  |
|----|----|----|----|
| http://www.hl7.org/Special/committees/fiwg/index.cfm | [Maturity Level](versions.html#maturity): [N](versions.html#std-process) |  [Normative](versions.html#std-process "Standard Status") (from v4.0.0) | [Compartments](compartmentdefinition.html): Not linked to any defined compartments |

|  |  |
|----|----|
|  | This page has been approved as part of an [ANSI ](https://www.ansi.org/) standard. See the [Infrastructure](ansi-infrastructure.html) Package for further details. |

## 2.26.1 Scope and Usage 

This specification defines a series of different types of resource that can be used to exchange and/or store data in order to solve a wide range of healthcare related problems, both clinical and administrative. In addition, this specification defines several different ways of exchanging the resources.

A resource is an entity that:

- has a known identity (a URL) by which it can be addressed
- identifies itself as one of the types of resource defined in this specification
- contains a set of structured data items as described by the definition of the resource type
- has an identified version that changes if the contents of the resource change

Resources have [multiple representations](formats.html).

## 2.26.2 Boundaries and Relationships 

The following optional elements and properties are defined for all resources:

- An identity
- Meta data
- A base language
- A reference to "Implicit Rules"

Most resources are derived from [DomainResource](domainresource.html) - so they also can contain text, contained resources, extensions, and data elements specific to the particular domain of the resource. There is a special type of resource called [Bundle](bundle.html) for collections of resources.

Note: there is documentation for the [Structure](formats.html), [UML](formats.html#uml), [XML](xml.html), and [JSON](json.html) representations of the resource structure.

## 2.26.3 Resource Content 

- [Structure](#tabs-struc)
- [UML](#tabs-uml)
- [XML](#tabs-xml)
- [JSON](#tabs-json)
- [Turtle](#tabs-ttl)
- [All](#tabs-all)

**Structure**

[TABLE]

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

\
\<[**\[name\]**](resource-definitions.html#Resource "This is the base resource type for everything.") xmlns="http://hl7.org/fhir"\> [](xml.html "Documentation for this format")\
 \<!-- from Element: [extension](extensibility.html) --\>\
 \<[**id**](resource-definitions.html#Resource.id "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.") value="\[[id](datatypes.html#id)\]"/\>\<!-- **0..1** [Logical id of this artifact](terminologies.html#unbound) --\>\
 \<[**meta**](resource-definitions.html#Resource.meta "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.")\>\<!-- **0..1** [Meta](resource.html#Meta) [Metadata about the resource](terminologies.html#unbound) --\>\</meta\>\
 \<[**implicitRules**](resource-definitions.html#Resource.implicitRules "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc (this element modifies the meaning of other elements)") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **0..1** [A set of rules under which this content was created](terminologies.html#unbound) --\>\
 \<[**language**](resource-definitions.html#Resource.language "The base language in which the resource is written.") value="\[[code](datatypes.html#code)\]"/\>\<!-- **0..1** [Language of the resource content](valueset-languages.html) --\>\
\</\[name\]\>\

**JSON Template**

\
{[](json.html "Documentation for this format")\
  "resourceType" : "[**\[name\]**](resource-definitions.html#Resource "This is the base resource type for everything.")",\
  "[id](resource-definitions.html#Resource.id "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.")" : "\<[id](datatypes.html#id)\>", // [Logical id of this artifact](terminologies.html#unbound)\
  "[meta](resource-definitions.html#Resource.meta "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.")" : { [Meta](resource.html#Meta) }, // [Metadata about the resource](terminologies.html#unbound)\
  "[implicitRules](resource-definitions.html#Resource.implicitRules "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc (this element modifies the meaning of other elements)")" : "\<[uri](datatypes.html#uri)\>", // [A set of rules under which this content was created](terminologies.html#unbound)\
  "[language](resource-definitions.html#Resource.language "The base language in which the resource is written.")" : "\<[code](datatypes.html#code)\>" // [Language of the resource content](valueset-languages.html)\
}\

**Turtle Template**

\
@prefix fhir: \<http://hl7.org/fhir/\> .[](rdf.html "Documentation for this format")\
\
\
\[ a fhir:[**\[name\]**](resource-definitions.html#Resource "This is the base resource type for everything.");\
  fhir:nodeRole fhir:treeRoot; # if this is the parser root\
\
 # from Element: [Element.extension](extensibility.html)\
  fhir:[Resource.id](resource-definitions.html#Resource.id "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.") \[ [id](datatypes.html#id) \]; # 0..1 Logical id of this artifact\
  fhir:[Resource.meta](resource-definitions.html#Resource.meta "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.") \[ [Meta](resource.html#Meta) \]; # 0..1 Metadata about the resource\
  fhir:[Resource.implicitRules](resource-definitions.html#Resource.implicitRules "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc (this element modifies the meaning of other elements)") \[ [uri](datatypes.html#uri) \]; # 0..1 A set of rules under which this content was created\
  fhir:[Resource.language](resource-definitions.html#Resource.language "The base language in which the resource is written.") \[ [code](datatypes.html#code) \]; # 0..1 Language of the resource content\
\]\

**Structure**

[TABLE]

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

\
\<[**\[name\]**](resource-definitions.html#Resource "This is the base resource type for everything.") xmlns="http://hl7.org/fhir"\> [](xml.html "Documentation for this format")\
 \<!-- from Element: [extension](extensibility.html) --\>\
 \<[**id**](resource-definitions.html#Resource.id "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.") value="\[[id](datatypes.html#id)\]"/\>\<!-- **0..1** [Logical id of this artifact](terminologies.html#unbound) --\>\
 \<[**meta**](resource-definitions.html#Resource.meta "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.")\>\<!-- **0..1** [Meta](resource.html#Meta) [Metadata about the resource](terminologies.html#unbound) --\>\</meta\>\
 \<[**implicitRules**](resource-definitions.html#Resource.implicitRules "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc (this element modifies the meaning of other elements)") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **0..1** [A set of rules under which this content was created](terminologies.html#unbound) --\>\
 \<[**language**](resource-definitions.html#Resource.language "The base language in which the resource is written.") value="\[[code](datatypes.html#code)\]"/\>\<!-- **0..1** [Language of the resource content](valueset-languages.html) --\>\
\</\[name\]\>\

**JSON Template**

\
{[](json.html "Documentation for this format")\
  "resourceType" : "[**\[name\]**](resource-definitions.html#Resource "This is the base resource type for everything.")",\
  "[id](resource-definitions.html#Resource.id "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.")" : "\<[id](datatypes.html#id)\>", // [Logical id of this artifact](terminologies.html#unbound)\
  "[meta](resource-definitions.html#Resource.meta "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.")" : { [Meta](resource.html#Meta) }, // [Metadata about the resource](terminologies.html#unbound)\
  "[implicitRules](resource-definitions.html#Resource.implicitRules "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc (this element modifies the meaning of other elements)")" : "\<[uri](datatypes.html#uri)\>", // [A set of rules under which this content was created](terminologies.html#unbound)\
  "[language](resource-definitions.html#Resource.language "The base language in which the resource is written.")" : "\<[code](datatypes.html#code)\>" // [Language of the resource content](valueset-languages.html)\
}\

**Turtle Template**

\
@prefix fhir: \<http://hl7.org/fhir/\> .[](rdf.html "Documentation for this format")\
\
\
\[ a fhir:[**\[name\]**](resource-definitions.html#Resource "This is the base resource type for everything.");\
  fhir:nodeRole fhir:treeRoot; # if this is the parser root\
\
 # from Element: [Element.extension](extensibility.html)\
  fhir:[Resource.id](resource-definitions.html#Resource.id "The logical id of the resource, as used in the URL for the resource. Once assigned, this value never changes.") \[ [id](datatypes.html#id) \]; # 0..1 Logical id of this artifact\
  fhir:[Resource.meta](resource-definitions.html#Resource.meta "The metadata about the resource. This is content that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.") \[ [Meta](resource.html#Meta) \]; # 0..1 Metadata about the resource\
  fhir:[Resource.implicitRules](resource-definitions.html#Resource.implicitRules "A reference to a set of rules that were followed when the resource was constructed, and which must be understood when processing the content. Often, this is a reference to an implementation guide that defines the special rules along with other profiles etc (this element modifies the meaning of other elements)") \[ [uri](datatypes.html#uri) \]; # 0..1 A set of rules under which this content was created\
  fhir:[Resource.language](resource-definitions.html#Resource.language "The base language in which the resource is written.") \[ [code](datatypes.html#code) \]; # 0..1 Language of the resource content\
\]\

### 2.26.3.1 Terminology Bindings 

| Path | Definition | Type | Reference |
|----|----|----|----|
| Resource.language | A human language. | [Preferred](terminologies.html#preferred), but limited to [AllLanguages](valueset-all-languages.html) | [CommonLanguages](valueset-languages.html) |

### 2.26.3.2 Resource Identity 

There are two different ways to identify a resource:

- By a "Location" URL that identifies where is can be accessed (based on the "Logical ID"). This location will be change as it is copied/moved around
- By some inherent identifier ("Business Identifier" or "Canonical URL") that is part of the resource and remains fixed as it is copied/moved around

### 2.26.3.3 Logical ID 

Each resource has an `id` element which contains the "logical id" of the resource assigned by the server responsible for storing it. Resources always have a known logical id except for a few special cases (e.g. when a new resource is being sent to a server to assign a logical id in the [create interaction](http.html#create)). The logical id is unique within the space of all resources of the same type on the same server. Once assigned by the server, the id is never changed.

The location of a resource instance is an absolute URI constructed from the server base address at which the instance is found, the resource type and the Logical ID, such as http://test.fhir.org/rest/Patient/123 (where `123` is the Logical Id of a [Patient](patient.html) resource). When the location is an HTTP address, this address can generally be used to retrieve or manipulate the resource. Note that implementations SHOULD NOT assume that the location of a resource is always resolvable to an accessible server - it may be temporarily unavailable, or not available by policy (e.g. firewalls) or in some cases, it might not actually exist (e.g. use of resource outside a RESTful environment). Resources reference each other by their location. These references are allowed to be absolute or relative (see [Resource References](references.html) for further discussion).

When a resource is copied from one server to another server, the copy might or might not keep the same logical id on the new server. This depends on replication and server policy. For further details, see [Managing Resource Identity](managing.html) (including "Consistent Resource Identification").

Logical ids (and therefore locations) are case sensitive. Logical Ids are always opaque, and external systems need not and should not attempt to determine their internal structure. A logical id SHALL always be represented in the same way in resource references and URLs. Ids can be up to 64 characters long, and contain any combination of upper and lowercase ASCII letters, numerals, "-" and ".".

In some contexts, resources are not associated with location on a RESTful server, either because they are only created transiently for transfer between systems, or the systems are not using RESTful servers. In these cases, resources may be assigned some kind of location anyway, for purposes of consistency, or they might not have an assigned logical id, and they are identified based on other kinds of identifiers. See [Resolving references in Bundles](bundle.html#references) for one method of using resources not associated with RESTful servers.

#### 2.26.3.3.1 "Business" Identifiers 

Although the logical id of a resource changes as it moves from server to server, all copies of the resource refer to the same underlying concept, and this concept may also be represented in other formats (variously, [HL7 v2 ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185), [CDA ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7), XDS, and many more). Each representation carries common identifiers that identify the underlying concept (also called "real world entity") consistently across all contexts of use. This is known as the `business identifier`, and is found in the *identifier* element, which has the type [Identifier](datatypes.html#Identifier).

All resources that have an `identifier` element support searching by the identifier, so that records can be located by that method. So if an [HL7 v2 ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185) message has the following OBR:

\
OBR\|1\|845439^GHH OE\|1045813^GHH LAB\|1554-5^GLUCOSE^LN\|\|\|200202150730\|...\

Then the DiagnosticReport it represents can be located using the following query:

\
 GET \[base\]/DiagnosticReport?identifier=1045813\

Most resources have a logical master server, the system on which the record first is created, and which manages the record directly. In the master system, the `Logical ID` might be the same value found in the business identifier since the master server can enforce business practices that make for stable identifiers. This is usually not a safe practice on secondary systems which are not in a position to enforce their required identifier consistency.

#### 2.26.3.3.2 Canonical URLs 

Some resource types have a defined element `url` which is the 'canonical URL' that always identifies the resource. This is a special kind of Business Identifier. Note that the element actually contains a URI, but is named `url` for legacy reasons.

The canonical URL serves as a stable logical identifier for the resource, and **is the preferred way to reference a conformance or knowledge resource**. The canonical URL SHOULD also resolve to the location where the master copy of the artifact is found, though it is not always possible to arrange this. The canonical URL SHALL NOT refer to some other resource (though it may resolve to a different version of the same resource).

See [Canonical references](references.html#canonical) for further discussion of canonical references and the [canonical data type](datatypes.html#canonical). The following resources have canonical URLs:

- [ActivityDefinition](activitydefinition.html)
- [CapabilityStatement](capabilitystatement.html)
- [ChargeItemDefinition](chargeitemdefinition.html)
- [CodeSystem](codesystem.html)
- [CompartmentDefinition](compartmentdefinition.html)
- [ConceptMap](conceptmap.html)
- [EffectEvidenceSynthesis](effectevidencesynthesis.html)
- [EventDefinition](eventdefinition.html)
- [Evidence](evidence.html)
- [EvidenceVariable](evidencevariable.html)
- [ExampleScenario](examplescenario.html)
- [GraphDefinition](graphdefinition.html)
- [ImplementationGuide](implementationguide.html)
- [Library](library.html)
- [Measure](measure.html)
- [MessageDefinition](messagedefinition.html)
- [NamingSystem](namingsystem.html)
- [OperationDefinition](operationdefinition.html)
- [PlanDefinition](plandefinition.html)
- [Questionnaire](questionnaire.html)
- [ResearchDefinition](researchdefinition.html)
- [ResearchElementDefinition](researchelementdefinition.html)
- [RiskEvidenceSynthesis](riskevidencesynthesis.html)
- [SearchParameter](searchparameter.html)
- [StructureDefinition](structuredefinition.html)
- [StructureMap](structuremap.html)
- [TerminologyCapabilities](terminologycapabilities.html)
- [TestScript](testscript.html)
- [ValueSet](valueset.html)

### 2.26.3.4 Consistent Resource Identification 

Business Identifiers are the preferred basis to recognize the same content on different systems. For example:

\
  GET http://a.company.example.com/Patient/23\
  \
  \<Patient xmlns="http://hl7.org/fhir"\>\
    \<id value="23"/\>\
    \<identifier\>  \
      \<system value="http://a.particular.system/identifier"/\>\
      \<value value="123456"/\>\
    \</identifier\>\
  \</Patient\>\
\
  GET http://other.company.example.com/fhir/Patient/5860200e-0ee3-42f5-8095-506e18dc9ca2\
  \
  \<Patient xmlns="http://hl7.org/fhir"\>\
    \<id value="5860200e-0ee3-42f5-8095-506e18dc9ca2"/\>\
    \<identifier\>  \
      \<system value="http://a.particular.system/identifier"/\>\
      \<value value="123456"/\>\
    \</identifier\>\
  \</Patient\>\

Given that the identifier is the same, the patient resources are understood to mean that they describe the same patient. For this reason, systems SHOULD:

- Only assign identifiers to resources when they uniquely identify the real world entity that the resources match (e.g. do not use account numbers as patient identifiers when multiple different patients share the same account number)
- Preserve identifiers as much as possible and not throw them away. Even if the identifiers are not useful to the system itself, they are likely to be useful to downstream consumers
- When serving resources, use consistent identifiers from the master persistent store where ever possible (e.g. when a resource is created from a primary record, populate the identifier, and store the identifier somewhere so the same identifier is used next time)

Following these practices will make for consistent identification of concepts and real-world entities across healthcare eco-systems. For example, medication orders can be represented as [MedicationRequest](medicationrequest.html) and [MedicationStatement](medicationstatement.html). Some systems - primary sources - will provide the medication order as a MedicationRequest while other secondary systems will provide them as a MedicationStatement. Any system processing the resources will need to reconcile these, and the presence of consistent identifiers will considerably simplify the reconciliation process.

Note that this specification provides two other related methods by which common source derivation can be indicated:

- [Provenance](provenance.html) - resources that have provenance statements where [Provenance.entity.what\[x\]](provenance-definitions.html#Provenance.entity.what_x_) refers to the same source, and the .entity.role is `derivation`
- [Resource.meta.source](resource-definitions.html#Meta.source) - two resources that have the same source

The granularity of [Provenance.entity.what\[x\]](provenance-definitions.html#Provenance.entity.what_x_) / [Resource.meta.source](resource-definitions.html#Meta.source) is not fixed to a single resource - multiple resources can be derived from a single source entity (e.g. a single CDA document), so applications need to be careful assuming that matching entity source information means that the resources are identifying the same real world concept.

### 2.26.3.5 Implicit Rules 

A reference to a custom agreement that describes how the resource is being used (e.g. an [implementation guide](profiling.html#glossary)) that was followed when the resource was constructed, where the implementation guide must be known and understood in order to safely processing the content.

Asserting this rule set restricts the content to be only understood by a limited set of trading partners. This inherently limits the usefulness of the data in the long term, and should be avoided where possible. However, the existing health eco-system is highly fractured, and not yet ready to define, collect, and exchange data in a generally exchangeable sense.

Note that resources are almost always constructed following some custom agreement. Best practice - which is recommended throughout the conformance resources - is that such agreements make all knowledge about the content of the resource explicit in the content of the resource; if custom agreements follow this advice, and declare their extensions as required, then it is not necessary to understand the agreement in order to safely process the resource content. For this reason, use of `implicitRules` is rare.

### 2.26.3.6 Language 

Each resource may have a language element that specifies the base language of the content using a [code defined in BCP 47 ](http://tools.ietf.org/html/bcp47). The language element is provided to support indexing and accessibility (e.g. text-to-speech use the language tag).

If a language is specified, it should also be specified on the [Narrative Text](narrative.html#Narrative). The html language tag in the narrative is used when processing the narrative. The language tag on the resource is provided so that applications processing the data in the resource can specify the language of any alternate presentations generated from the data.

There is no default language, though one may be inferred from the context of use. Not all of the content of the resource has to be in the specified language. [Multiple languages](languages.html) can be supported.

Any valid language code as defined in [BCP 47 ](http://tools.ietf.org/html/bcp47) is valid. The language code system is complex, with parts for Primary Language, Script, Region, and other variants and extensions. In order to simplify implementations, the language element has a [preferred binding](terminologies.html#preferred) to an enumerated list of common language codes encountered in applications, with translations, and also a [maximum binding](extension-elementdefinition-maxvalueset.html) of any language; this allows most applications to simply use a look up table, without preventing the use of any language code.

### 2.26.3.7 Resource Metadata 

Each resource contains an element "meta", of type "Meta", which is a set of metadata that provides technical and workflow context to the resource. The metadata items are all optional, though some or all of them may be required in particular implementations or contexts of use.

[TABLE]

- [Structure](#tabs-Meta-struc)
- [UML](#tabs-Meta-uml)
- [XML](#tabs-Meta-xml)
- [JSON](#tabs-Meta-json)
- [Turtle](#tabs-Meta-ttl)
- [R3 Diff](#tabs-Meta-diff)
- [All](#tabs-Meta-all)

**Structure**

[TABLE]

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

\
\<[**meta**](resource-definitions.html#Meta "The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.") xmlns="http://hl7.org/fhir"\>\
 \<!-- from Element: [extension](extensibility.html) --\>\
 \<[**versionId**](resource-definitions.html#Meta.versionId "The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted.") value="\[[id](datatypes.html#id)\]"/\>\<!-- **0..1** [Version specific identifier](terminologies.html#unbound) --\>\
 \<[**lastUpdated**](resource-definitions.html#Meta.lastUpdated "When the resource last changed - e.g. when the version changed.") value="\[[instant](datatypes.html#instant)\]"/\>\<!-- **0..1** [When the resource version last changed](terminologies.html#unbound) --\>\
 \<[**source**](resource-definitions.html#Meta.source "A uri that identifies the source system of the resource. This provides a minimal amount of [[[Provenance]]] information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc.") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **0..1** [Identifies where the resource comes from](terminologies.html#unbound) --\>\
 \<[**profile**](resource-definitions.html#Meta.profile "A list of profiles (references to [[[StructureDefinition]]] resources) that this resource claims to conform to. The URL is a reference to [[[StructureDefinition.url]]].")\>\<!-- **0..\*** [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html#StructureDefinition)) [Profiles this resource claims to conform to](terminologies.html#unbound) --\>\</profile\>\
 \<[**security**](resource-definitions.html#Meta.security "Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure.")\>\<!-- **0..\*** [Coding](datatypes.html#Coding) [Security Labels applied to this resource](valueset-security-labels.html) --\>\</security\>\
 \<[**tag**](resource-definitions.html#Meta.tag "Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource.")\>\<!-- **0..\*** [Coding](datatypes.html#Coding) [Tags applied to this resource](valueset-common-tags.html) --\>\</tag\>\
\</meta\>\

**JSON Template**

\
{[](json.html "Documentation for this format")\
  // from Element: [extension](extensibility.html)\
  "[versionId](resource-definitions.html#Meta.versionId "The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted.")" : "\<[id](datatypes.html#id)\>", // [Version specific identifier](terminologies.html#unbound)\
  "[lastUpdated](resource-definitions.html#Meta.lastUpdated "When the resource last changed - e.g. when the version changed.")" : "\<[instant](datatypes.html#instant)\>", // [When the resource version last changed](terminologies.html#unbound)\
  "[source](resource-definitions.html#Meta.source "A uri that identifies the source system of the resource. This provides a minimal amount of [[[Provenance]]] information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc.")" : "\<[uri](datatypes.html#uri)\>", // [Identifies where the resource comes from](terminologies.html#unbound)\
  "[profile](resource-definitions.html#Meta.profile "A list of profiles (references to [[[StructureDefinition]]] resources) that this resource claims to conform to. The URL is a reference to [[[StructureDefinition.url]]].")" : \[{ [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html#StructureDefinition)) }\], // [Profiles this resource claims to conform to](terminologies.html#unbound)\
  "[security](resource-definitions.html#Meta.security "Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure.")" : \[{ [Coding](datatypes.html#Coding) }\], // [Security Labels applied to this resource](valueset-security-labels.html)\
  "[tag](resource-definitions.html#Meta.tag "Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource.")" : \[{ [Coding](datatypes.html#Coding) }\] // [Tags applied to this resource](valueset-common-tags.html)\
}\

**Turtle Template**

\
@prefix fhir: \<http://hl7.org/fhir/\> .\
\
\[\
 # from Element: [Element.extension](extensibility.html)\
  fhir:[Meta.versionId](resource-definitions.html#Meta.versionId "The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted.") \[ [id](datatypes.html#id) \]; # 0..1 Version specific identifier\
  fhir:[Meta.lastUpdated](resource-definitions.html#Meta.lastUpdated "When the resource last changed - e.g. when the version changed.") \[ [instant](datatypes.html#instant) \]; # 0..1 When the resource version last changed\
  fhir:[Meta.source](resource-definitions.html#Meta.source "A uri that identifies the source system of the resource. This provides a minimal amount of [[[Provenance]]] information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc.") \[ [uri](datatypes.html#uri) \]; # 0..1 Identifies where the resource comes from\
  fhir:[Meta.profile](resource-definitions.html#Meta.profile "A list of profiles (references to [[[StructureDefinition]]] resources) that this resource claims to conform to. The URL is a reference to [[[StructureDefinition.url]]].") \[ [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html#StructureDefinition)) \], ... ; # 0..\* Profiles this resource claims to conform to\
  fhir:[Meta.security](resource-definitions.html#Meta.security "Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure.") \[ [Coding](datatypes.html#Coding) \], ... ; # 0..\* Security Labels applied to this resource\
  fhir:[Meta.tag](resource-definitions.html#Meta.tag "Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource.") \[ [Coding](datatypes.html#Coding) \], ... ; # 0..\* Tags applied to this resource\
\]\

**Changes since Release 3**

[TABLE]

See the [Full Difference](diff.html) for further information

**Structure**

[TABLE]

**UML Diagram** ([Legend](formats.html#uml))

**XML Template**

\
\<[**meta**](resource-definitions.html#Meta "The metadata about a resource. This is content in the resource that is maintained by the infrastructure. Changes to the content might not always be associated with version changes to the resource.") xmlns="http://hl7.org/fhir"\>\
 \<!-- from Element: [extension](extensibility.html) --\>\
 \<[**versionId**](resource-definitions.html#Meta.versionId "The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted.") value="\[[id](datatypes.html#id)\]"/\>\<!-- **0..1** [Version specific identifier](terminologies.html#unbound) --\>\
 \<[**lastUpdated**](resource-definitions.html#Meta.lastUpdated "When the resource last changed - e.g. when the version changed.") value="\[[instant](datatypes.html#instant)\]"/\>\<!-- **0..1** [When the resource version last changed](terminologies.html#unbound) --\>\
 \<[**source**](resource-definitions.html#Meta.source "A uri that identifies the source system of the resource. This provides a minimal amount of [[[Provenance]]] information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc.") value="\[[uri](datatypes.html#uri)\]"/\>\<!-- **0..1** [Identifies where the resource comes from](terminologies.html#unbound) --\>\
 \<[**profile**](resource-definitions.html#Meta.profile "A list of profiles (references to [[[StructureDefinition]]] resources) that this resource claims to conform to. The URL is a reference to [[[StructureDefinition.url]]].")\>\<!-- **0..\*** [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html#StructureDefinition)) [Profiles this resource claims to conform to](terminologies.html#unbound) --\>\</profile\>\
 \<[**security**](resource-definitions.html#Meta.security "Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure.")\>\<!-- **0..\*** [Coding](datatypes.html#Coding) [Security Labels applied to this resource](valueset-security-labels.html) --\>\</security\>\
 \<[**tag**](resource-definitions.html#Meta.tag "Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource.")\>\<!-- **0..\*** [Coding](datatypes.html#Coding) [Tags applied to this resource](valueset-common-tags.html) --\>\</tag\>\
\</meta\>\

**JSON Template**

\
{[](json.html "Documentation for this format")\
  // from Element: [extension](extensibility.html)\
  "[versionId](resource-definitions.html#Meta.versionId "The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted.")" : "\<[id](datatypes.html#id)\>", // [Version specific identifier](terminologies.html#unbound)\
  "[lastUpdated](resource-definitions.html#Meta.lastUpdated "When the resource last changed - e.g. when the version changed.")" : "\<[instant](datatypes.html#instant)\>", // [When the resource version last changed](terminologies.html#unbound)\
  "[source](resource-definitions.html#Meta.source "A uri that identifies the source system of the resource. This provides a minimal amount of [[[Provenance]]] information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc.")" : "\<[uri](datatypes.html#uri)\>", // [Identifies where the resource comes from](terminologies.html#unbound)\
  "[profile](resource-definitions.html#Meta.profile "A list of profiles (references to [[[StructureDefinition]]] resources) that this resource claims to conform to. The URL is a reference to [[[StructureDefinition.url]]].")" : \[{ [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html#StructureDefinition)) }\], // [Profiles this resource claims to conform to](terminologies.html#unbound)\
  "[security](resource-definitions.html#Meta.security "Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure.")" : \[{ [Coding](datatypes.html#Coding) }\], // [Security Labels applied to this resource](valueset-security-labels.html)\
  "[tag](resource-definitions.html#Meta.tag "Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource.")" : \[{ [Coding](datatypes.html#Coding) }\] // [Tags applied to this resource](valueset-common-tags.html)\
}\

**Turtle Template**

\
@prefix fhir: \<http://hl7.org/fhir/\> .\
\
\[\
 # from Element: [Element.extension](extensibility.html)\
  fhir:[Meta.versionId](resource-definitions.html#Meta.versionId "The version specific identifier, as it appears in the version portion of the URL. This value changes when the resource is created, updated, or deleted.") \[ [id](datatypes.html#id) \]; # 0..1 Version specific identifier\
  fhir:[Meta.lastUpdated](resource-definitions.html#Meta.lastUpdated "When the resource last changed - e.g. when the version changed.") \[ [instant](datatypes.html#instant) \]; # 0..1 When the resource version last changed\
  fhir:[Meta.source](resource-definitions.html#Meta.source "A uri that identifies the source system of the resource. This provides a minimal amount of [[[Provenance]]] information that can be used to track or differentiate the source of information in the resource. The source may identify another FHIR server, document, message, database, etc.") \[ [uri](datatypes.html#uri) \]; # 0..1 Identifies where the resource comes from\
  fhir:[Meta.profile](resource-definitions.html#Meta.profile "A list of profiles (references to [[[StructureDefinition]]] resources) that this resource claims to conform to. The URL is a reference to [[[StructureDefinition.url]]].") \[ [canonical](datatypes.html#canonical)([StructureDefinition](structuredefinition.html#StructureDefinition)) \], ... ; # 0..\* Profiles this resource claims to conform to\
  fhir:[Meta.security](resource-definitions.html#Meta.security "Security labels applied to this resource. These tags connect specific resources to the overall security policy and infrastructure.") \[ [Coding](datatypes.html#Coding) \], ... ; # 0..\* Security Labels applied to this resource\
  fhir:[Meta.tag](resource-definitions.html#Meta.tag "Tags applied to this resource. Tags are intended to be used to identify and relate resources to process and workflow, and applications are not required to consider the tags when interpreting the meaning of a resource.") \[ [Coding](datatypes.html#Coding) \], ... ; # 0..\* Tags applied to this resource\
\]\

**Changes since Release 3**

[TABLE]

See the [Full Difference](diff.html) for further information

Note that the RESTful API defines some [Operations](operations.html) that provide [direct read and write access](resource-operation-meta.html) to the *meta* element.

#### 2.26.3.7.1 Record Versions vs Business Versions vs FHIR Versions 

There are 3 different versions of interest for a resource:

1.  The Record Version: changes each time the resource changes (usually managed by a server)
2.  The Business version: changes each time the content in the resources changes (managed by a human author or by business policy)
3.  The FHIR Version: the version of FHIR in which the resource is represented (controlled by the author of the resource)

**Record (Resource) Version**

All resources are conceptually versioned, and each resource sits at the head of a linear list of past versions. The past versions are superseded by the current version, and only available for audit/integrity purposes. The current version is e.g. http://acme.org/fhir/ResourceType/id123, and a past version would be http://acme.org/fhir/ResourceType/id123/\_history/v2.

Note that there's no requirement for servers to keep a history. The [history interaction](http.html#history) is provided for where this is an appropriate service to provide. However, whether a server keeps them or not, past versions are dead and gone. The current version of the resource is in the *Resource.meta.versionId*. For a value set this would be:

\
\<ValueSet\>\
  \<meta\>\
    \<versionId value="v2"/\>\
  \</meta\>\
\</ValueSet\>\

The versionId changes every time the server updates the resource and writes a new version over the top of an existing one.

**Business Version**

Some resources have another version marker in them. For instance, ValueSet has another version in it:

\
\<ValueSet\>\
  \<url value="http://acme.com/fhir/ValueSet/example"/\>\
  \<version value="2.0"/\>\
\</ValueSet\>\

This says that this is version 2.0 of the 'example' value set. This is the business version of the value set, the one that humans get involved with. These 2 versions elements have quite different lifecycles. To illustrate, take these cases:

1.  A value set is posted to a server (POST \[base\]/ValueSet) with ValueSet.url = "http://acme.com/valuesets/example". This is identified as the 1st version of the value set (ValueSet.version = 1). When the server gets it, it assigns an identity e.g. ValueSet.id = x1, and ValueSet.meta.versionId = 1. Later, another user creates a revised version of the value set, and this is called version 2. It is committed to the server as an update (PUT \[base\]/ValueSet/x1).\
    Now, ValueSet.url = http://acme.com/valuesets/example, ValueSet.id = x1, ValueSet.version = 2 and ValueSet.meta.versionId = 2
2.  A value set is posted to a server (POST \[base\]/ValueSet) with ValueSet.url = "http://acme.com/valuesets/example". This is identified as the 1st version of the value set (ValueSet.version = 1). When the server gets it, it assigns an identity e.g. ValueSet.id = x1, and ValueSet.meta.versionId = 1. Then a typo is found in the definition, so this is fixed, but it's still v1 of the value set. This is PUT to \[base\]/ValueSet/x1. Now, ValueSet.url = http://acme.com/valuesets/example, ValueSet.id = x1, ValueSet.version = 1 and ValueSet.meta.versionId = 2.\
    Later, another user creates a revised version of the value set, and this is called version 2. It is commited to the server as an update (PUT \[base\]/ValueSet/x1). Now, ValueSet.url = http://acme.com/valuesets/example, ValueSet.id = x1, ValueSet.version = 2 and ValueSet.meta.versionId = 3
3.  A value set is posted to a server (POST \[base\]/ValueSet) with ValueSet.url = "http://acme.com/valuesets/example". This is identified as the 1st version of the value set (ValueSet.version = 1). When the server gets it, it assigns an identity e.g. ValueSet.id = x1, and ValueSet.meta.versionId = 1. Later, another user creates a revised version of the value set, and this is called version 2. This time, as well as supporting this new version 2, there are production systems still using version 1, and both need to be valid on the value set server. So a new value set is created on the server (POST \[base\]/ValueSet) and is assigned the identiity 'x2'.\
    Now, there are two different value sets, both with URL "http://acme.com/valuesets/example". One has ValueSet.id = x1, ValueSet.version = 1 and ValueSet.meta.versionId = 1 and the other has ValueSet.id = x2, ValueSet.version = 2 and ValueSet.meta.versionId = 1.

The version of resource SHOULD change every time some non-significant change is made. Exactly what change constitutes 'significant' depends on context, and is not specified here. Note, though, that it is possible to change elements such as `status` and `date` without changing the version, such as when marking a past version as `retired`. In general, any other changes should be associated with a change in version.

The [Semantic Versioning ](https://semver.org/) specification recommend that versions be represented in three parts using the form MAJOR.MINOR.PATCH where, for the kind of artefacts described in this specification:

- MAJOR version increments when incompatible changes are made to the artifact
- MINOR version increments functionality is added to an artefact in a backwards-compatible manner
- PATCH version increments when minor changes are made that don't impact on implementations of the artefact (e.g. documentation clarifications)

For the kind of resources that have [canonical URLs](#canonical), this specification recommends that implementers follow the Semantic Versioning principles, but does not require this. Implementers should consider, however, making the MAJOR version part of the [canonical URL](#canonical) rather than putting it in `[Resource].version`. So instead of this:

\
{ \
  "resourceType" : "ValueSet",\
  "url" : "http://example.org/fhir/ValueSet/blah",\
  "version" : "2.1.1"\
 }\

implementers should instead consider:

\
{ \
  "resourceType" : "ValueSet",\
  "url" : "http://example.org/fhir/ValueSet/blah2",\
  "version" : "1.1"\
 }\

The principle advantage is that other artefacts that reference the first artefact can do so by major version:

\
  "binding" : { \
     "valueSet" : "http://example.org/fhir/ValueSet/blah2"\
  }\

The alternative - not having the major version in the URL - means that version dependencies must be managed by some other method (e.g. managing a set of resources with specific versioned references via an [Implementation Guide](implementationguide.html)).

There is no single best practice here; the correct choice depends on many factors outside the scope of this specification.

**FHIR Version**

All resources always have a FHIR version against which they were written. Note, however, that resources may be valid against multiple different FHIR versions, and this becomes progressively more likely as the [maturity of the resource](versions.html#maturity) progresses.

The version is often not stated explicitly in the resource; it is controlled by the context. See [Managing Multiple FHIR versions](versioning.html) for further information.

### 2.26.3.8 Tags, Profiles, and Security Labels 

These 3 metadata attributes are part of the resource, but are never used to keep information that needs to be understood when interpreting the content of a resource; their function is limited to finding and controlling access to the resource, and connecting resources to technical or clinical workflow.

#### 2.26.3.8.1 Tags 

Tags are used to associate additional operational information with the Resources, such as workflow management. A typical use of tagging would be to maintain an informal list of resources that need review.

In a general tag, the [coded concept](datatypes.html#coding) may be a reference to a healthcare vocabulary, including ones defined in this specification, or vocabularies such as those defined by HL7 for other purposes (e.g. [HL7 v2 ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185) and [HL7 v3 ](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=186)/[CDA ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7)), LOINC, or SNOMED CT. Alternatively, the concept may be one defined by the implementation in the local context.

The list of tags on a resource is a set, where each tag is unique based on the `system`+`code` combination.

#### 2.26.3.8.2 Profile Tags 

A profile assertion represents a claim that the resource conforms to [the identified StructureDefinition](structuredefinition.html), which makes rules about what content is allowed to be in a resource. In a profile tag, the term is a URL that references an identified [StructureDefinition](structuredefinition.html) resource.

It's always possible to determine whether a resource conforms to any profile simply by testing it against the profile (the [validation tools](downloads.html) provide the functionality to perform this test in a variety of contexts). However there are several circumstances where simply examining whether a resource conforms to a particular profile as needed is impractical:

- A server searching a set of resources for ones that conform to a particular profile
- A receiver that has many profiles to choose when validating resource

Profile Tags serve these use cases - a client/creator of a resource can tag the resource with an assertion that the resource conforms to a particular structure definition. The server/receiver of the resource can choose to take this assertion at face value, or to assist in locating the correct [StructureDefinition](structuredefinition.html) against which to validate the resource.

Note: resources can conform to multiple profiles at once. A resource can conform to a profile without ever being labeled that it does, or a resource may falsely claim to conform to a profile. For this reason, applications processing resources SHOULD always depend on the contents of the resource when processing them, and/or check resources against the [StructureDefinition](structuredefinition.html)s directly rather than relying the existence of profile tags for meaning. Profile Tags are provided as a method of finding resources that conform to a particular [StructureDefinition](structuredefinition.html), not statements of meaning about the resource.

Many trading partner agreements will make rules about what claims can be made and when they must be tested, which will make the profile assertion more reliable.

The list of profiles on a resource is a set, where each profile is unique based on the `value` of the URI.

#### 2.26.3.8.3 Security Labels 

A security label is attached to a resource to provide specific security metadata about the information in the resource. For further information, see [Security Labels](security-labels.html).

The list of security labels on a resource is a set, where each tag is unique based on the `system`+`code` combination.

### 2.26.3.9 Updates to Tags, Profiles, and Security Labels 

When a resource is updated (e.g. on the RESTful interface), servers generally follow this pattern:

- Merge existing and new tags
- Replace existing profile tags with new profile tags
- Merge existing and new security labels

However, in some cases, an update may invalidate existing tags. Servers may update or remove previously existing recognized tags if this is known to be appropriate.

### 2.26.3.10 Further Information 

- [Conformance Rules](conformance-rules.html)
- [Resource Definitions](resourcelist.html)
- [References between Resources](references.html)
- [Narratives](narrative.html)
- [Formats:](formats.html) [XML](xml.html), [JSON](json.html)
- [Extensibility](extensibility.html) ([Examples](extensibility-examples.html))
- [Detailed Descriptions](resource-definitions.html)
- [Inter-version Compatibility](versions.html)

### 2.26.3.11 Maturity Levels 

The [Maturity level documentation has moved](versions.html#maturity).

## 2.26.4 Search Parameters 

Common search parameters defined by this resource. See [Searching](search.html) for more information about searching in REST, messaging, and services.

|  |  |  |  |
|----|----|----|----|
| **Name** | **Type** | **Description** | **Paths** |
| \_content | [string](search.html#string) | Search on the entire content of the resource |  |
| \_id | [token](search.html#token) | Logical id of this artifact | Resource.id |
| \_lastUpdated | [date](search.html#date) | When the resource version last changed | Resource.meta.lastUpdated |
| \_profile | [uri](search.html#uri) | Profiles this resource claims to conform to | Resource.meta.profile |
| \_query | [token](search.html#token) | A custom search profile that describes a specific defined query operation |  |
| \_security | [token](search.html#token) | Security Labels applied to this resource | Resource.meta.security |
| \_source | [uri](search.html#uri) | Identifies where the resource comes from | Resource.meta.source |
| \_tag | [token](search.html#token) | Tags applied to this resource | Resource.meta.tag |

®© HL7.org 2011+. FHIR Release 4 (Technical Correction \#1) (v4.0.1) generated on Fri, Nov 1, 2019 09:34+1100. [QA Page](qa.html)\
Links: [Search ](http://hl7.org/fhir/search.cfm) \| [Version History](history.html) \| [Table of Contents](toc.html) \| [Credits](credits.html) \| [Compare to R3 ](https://www.fhir.org/perl/htmldiff.pl?oldfile=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fresource.html&newfile=http%3A%2F%2Fhl7.org%2Ffhir%2FR4%2Fresource.html) \| [](license.html) \| [Propose a change ](http://hl7.org/fhir-issues)
