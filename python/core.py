# Auto generated from core.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-21 16:17
# Schema: Alliance-Schema-Prototype-Core-Types
#
# id: https://github.com/alliance-genome/agr_persistent_schema/core.yaml
# description: Alliance Schema Prototype with LinkML
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml.utils.slot import Slot
from linkml.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml.utils.formatutils import camelcase, underscore, sfx
from linkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml.utils.curienamespace import CurieNamespace
from . crossReference import CrossReferenceCrossReferenceId
from . informationContentEntity import InformationContentEntity
from linkml.utils.metamodelcore import Bool, URIorCURIE, XSDDate
from linkml_model.types import Boolean, Date, String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ENSEMBL = CurieNamespace('ENSEMBL', 'http://identifiers.org/ensembl/')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
HGNC = CurieNamespace('HGNC', 'http://identifiers.org/hgnc/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
RGD = CurieNamespace('RGD', 'http://identifiers.org/rgd/')
SGD = CurieNamespace('SGD', 'http://identifiers.org/sgd/')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
ZFIN = CurieNamespace('ZFIN', 'http://identifiers.org/zfin/')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'https://www.w3.org/TR/skos-reference/#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = ALLIANCE


# Types
class BiologicalSequence(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "biological sequence"
    type_model_uri = ALLIANCE.BiologicalSequence


# Class references
class GeneGeneId(extended_str):
    pass


class TranscriptTranscriptId(extended_str):
    pass


class GenomicEntity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity
    class_class_curie: ClassVar[str] = "alliance:GenomicEntity"
    class_name: ClassVar[str] = "genomic entity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.GenomicEntity


@dataclass
class Gene(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Gene
    class_class_curie: ClassVar[str] = "alliance:Gene"
    class_name: ClassVar[str] = "gene"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Gene

    gene_id: Union[str, GeneGeneId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gene_id is None:
            raise ValueError("gene_id must be supplied")
        if not isinstance(self.gene_id, GeneGeneId):
            self.gene_id = GeneGeneId(self.gene_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Transcript(YAMLRoot):
    """
    An RNA synthesized on a DNA or RNA template by an RNA polymerase.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Transcript
    class_class_curie: ClassVar[str] = "alliance:Transcript"
    class_name: ClassVar[str] = "transcript"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Transcript

    transcript_id: Union[str, TranscriptTranscriptId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.transcript_id is None:
            raise ValueError("transcript_id must be supplied")
        if not isinstance(self.transcript_id, TranscriptTranscriptId):
            self.transcript_id = TranscriptTranscriptId(self.transcript_id)

        super().__post_init__(**kwargs)


@dataclass
class Allele(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Allele
    class_class_curie: ClassVar[str] = "alliance:Allele"
    class_name: ClassVar[str] = "allele"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Allele

    allele_id: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.allele_id is None:
            raise ValueError("allele_id must be supplied")
        if not isinstance(self.allele_id, str):
            self.allele_id = str(self.allele_id)

        super().__post_init__(**kwargs)


class Species(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Species
    class_class_curie: ClassVar[str] = "alliance:Species"
    class_name: ClassVar[str] = "species"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Species


class Annotation(YAMLRoot):
    """
    Biolink Model root class for entity annotations.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.Annotation
    class_class_curie: ClassVar[str] = "alliance:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.Annotation


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=ALLIANCE.id, name="id", curie=ALLIANCE.curie('id'),
                   model_uri=ALLIANCE.id, domain=None, range=URIRef)

slots.date_produced = Slot(uri=ALLIANCE.date_produced, name="date_produced", curie=ALLIANCE.curie('date_produced'),
                   model_uri=ALLIANCE.date_produced, domain=None, range=Optional[Union[str, XSDDate]])

slots.release = Slot(uri=ALLIANCE.release, name="release", curie=ALLIANCE.curie('release'),
                   model_uri=ALLIANCE.release, domain=None, range=Optional[str])

slots.data_provider = Slot(uri=ALLIANCE.data_provider, name="data provider", curie=ALLIANCE.curie('data_provider'),
                   model_uri=ALLIANCE.data_provider, domain=None, range=Optional[Union[str, List[str]]])

slots.description = Slot(uri=ALLIANCE.description, name="description", curie=ALLIANCE.curie('description'),
                   model_uri=ALLIANCE.description, domain=None, range=Optional[str])

slots.name = Slot(uri=ALLIANCE.name, name="name", curie=ALLIANCE.curie('name'),
                   model_uri=ALLIANCE.name, domain=None, range=Optional[str])

slots.cross_references = Slot(uri=ALLIANCE.cross_references, name="cross references", curie=ALLIANCE.curie('cross_references'),
                   model_uri=ALLIANCE.cross_references, domain=None, range=Optional[Union[Union[str, CrossReferenceCrossReferenceId], List[Union[str, CrossReferenceCrossReferenceId]]]])

slots.symbol = Slot(uri=ALLIANCE.symbol, name="symbol", curie=ALLIANCE.curie('symbol'),
                   model_uri=ALLIANCE.symbol, domain=None, range=Optional[str])

slots.from_species = Slot(uri=ALLIANCE.from_species, name="from species", curie=ALLIANCE.curie('from_species'),
                   model_uri=ALLIANCE.from_species, domain=None, range=Optional[Union[dict, Species]])

slots.synonym = Slot(uri=ALLIANCE.synonym, name="synonym", curie=ALLIANCE.curie('synonym'),
                   model_uri=ALLIANCE.synonym, domain=None, range=Optional[Union[str, List[str]]])

slots.negated = Slot(uri=ALLIANCE.negated, name="negated", curie=ALLIANCE.curie('negated'),
                   model_uri=ALLIANCE.negated, domain=None, range=Optional[Union[bool, Bool]])

slots.qualifiers = Slot(uri=ALLIANCE.qualifiers, name="qualifiers", curie=ALLIANCE.curie('qualifiers'),
                   model_uri=ALLIANCE.qualifiers, domain=InformationContentEntity, range=Optional[str])

slots.synonyms = Slot(uri=ALLIANCE.synonyms, name="synonyms", curie=ALLIANCE.curie('synonyms'),
                   model_uri=ALLIANCE.synonyms, domain=None, range=Optional[str])

slots.type = Slot(uri=ALLIANCE.type, name="type", curie=ALLIANCE.curie('type'),
                   model_uri=ALLIANCE.type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.gene_gene_id = Slot(uri=ALLIANCE.gene_id, name="gene_gene id", curie=ALLIANCE.curie('gene_id'),
                   model_uri=ALLIANCE.gene_gene_id, domain=Gene, range=Union[str, GeneGeneId])

slots.transcript_transcript_id = Slot(uri=ALLIANCE.transcript_id, name="transcript_transcript id", curie=ALLIANCE.curie('transcript_id'),
                   model_uri=ALLIANCE.transcript_transcript_id, domain=Transcript, range=Union[str, TranscriptTranscriptId])
