# 2.17   Introducing HL7 FHIR 

|  |  |  |
|----|----|----|
| [FHIR Infrastructure ](http://www.hl7.org/Special/committees/fiwg/index.cfm) Work Group | [Maturity Level](versions.html#maturity): N/A | [Standards Status](versions.html#std-process): [Informative](versions.html#std-process) |

FHIR® – Fast Healthcare Interoperability Resources (hl7.org/fhir) – is a next generation standards framework created by HL7. FHIR combines the best features of HL7's [v2 ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185), [HL7 v3 ](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=186) and [CDA ](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=7) product lines while leveraging the latest web standards and applying a tight focus on implementability.

FHIR solutions are built from a set of modular components called "Resources". These resources can easily be assembled into working systems that solve real world clinical and administrative problems at a fraction of the price of existing alternatives. FHIR is suitable for use in a wide variety of contexts – mobile phone apps, cloud communications, EHR-based data sharing, server communication in large institutional healthcare providers, and much more.

## 2.17.1   Why FHIR is better 

FHIR offers many improvements over existing standards:

- A strong focus on implementation: fast and easy to implement (multiple developers have had simple interfaces working in a single day)
- Multiple implementation libraries, many examples available to kick-start development
- Specification is free for use with no restrictions
- Interoperability out-of-the-box: base resources can be used as is, but can also be adapted as needed - which happens a lot - for local requirements using Profiles, Extensions, Terminologies and more
- Evolutionary development path from HL7 Version 2 and CDA: standards can co-exist and leverage each other
- Strong foundation in Web standards: XML, JSON, HTTP, OAuth, etc.
- Support for RESTful architectures, seamless exchange of information using messages or documents, and service-based architectures
- Concise and easily understood specifications
- A human-readable serialization format for ease of use by developers
- Ontology-based analysis with formal mapping for correctness (under development)

## 2.17.2 Flexibility / Adaptation 

A central challenge for healthcare standards is how to handle the wide variability caused by diverse healthcare processes. Over time, more fields and optionality are added to the specification, gradually adding cost and complexity to the resulting implementations. The alternative is relying on custom extensions, but these create many implementation problems too.

FHIR solves this challenge by defining a simple framework for extending the existing resources and describing their use with Profiles. All systems can read all resources, but applications can add more control and meaning using profiles. Many healthcare contexts require extensive local agreements.

In addition, each resource carries a human-readable text representation using html as a fall-back display option for clinical safety. This is particularly important for complex clinical information where many systems take a simple textual/document based approach.

## 2.17.3   Example Resource: Patient 

This simple example shows the important parts of a resource: a local extension, the human readable HTML presentation, and the standard defined data content.

FHIR has resources for administrative concepts such as patient, provider, organization and device as well as a wide variety of clinical concepts covering problems, medications, diagnostics, care plans, financial concerns and more.

## 2.17.4 The FHIR development process 

FHIR is published as a mixed standard with Normative portions, which are kept stable for implementers, and also parts still undergoing Trial Use. HL7 actively monitors implementations in order to continue to improve the specification to be responsive to their needs. Due to the many advantages FHIR offers, FHIR is widely used around the world, and the implementation community is growing quickly.

[http://hl7.org/fhir ](http://hl7.org/fhir). Follow us on Twitter using [\#FHIR ](https://twitter.com/search?q=%23FHIR)

®© HL7.org 2011+. FHIR Release 4 (Technical Correction \#1) (v4.0.1) generated on Fri, Nov 1, 2019 09:37+1100. [QA Page](qa.html)\
Links: [Search ](http://hl7.org/fhir/search.cfm) \| [Version History](history.html) \| [Table of Contents](toc.html) \| [Credits](credits.html) \| [Compare to R3 ](https://www.fhir.org/perl/htmldiff.pl?oldfile=http%3A%2F%2Fhl7.org%2Ffhir%2FSTU3%2Fsummary.html&newfile=http%3A%2F%2Fhl7.org%2Ffhir%2FR4%2Fsummary.html) \| [](license.html) \| [Propose a change ](http://hl7.org/fhir-issues)
