# Auto generated from genomic.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-27 08:49
# Schema: Alliance-Schema-Prototype-Variation
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic
# description:
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
from . core import GenomicEntity
from . variation import VariantId
from linkml.utils.metamodelcore import URIorCURIE
from linkml_model.types import String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FALDO = CurieNamespace('faldo', 'http://biohackathon.org/resource/faldo#')
GFF = CurieNamespace('gff', 'https://w3id.org/gff')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/')


# Types

# Class references
class ChromosomeId(URIorCURIE):
    pass


@dataclass
class Chromosome(YAMLRoot):
    """
    The ID of the landmark used to establish the coordinate system for the current feature.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/Chromosome")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "chromosome"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/Chromosome")

    id: Union[str, ChromosomeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ChromosomeId):
            self.id = ChromosomeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GeneGenomicLocation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/GeneGenomicLocation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "gene genomic location"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/GeneGenomicLocation")

    subject: Union[str, VariantId] = None
    predicate: str = None
    object: Union[str, ChromosomeId] = None
    assembly: str = None
    start: Optional[str] = None
    end: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, VariantId):
            self.subject = VariantId(self.subject)

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, ChromosomeId):
            self.object = ChromosomeId(self.object)

        if self.assembly is None:
            raise ValueError("assembly must be supplied")
        if not isinstance(self.assembly, str):
            self.assembly = str(self.assembly)

        if self.start is not None and not isinstance(self.start, str):
            self.start = str(self.start)

        if self.end is not None and not isinstance(self.end, str):
            self.end = str(self.end)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.start = Slot(uri=DEFAULT_.start, name="start", curie=DEFAULT_.curie('start'),
                   model_uri=DEFAULT_.start, domain=None, range=Optional[str])

slots.end = Slot(uri=DEFAULT_.end, name="end", curie=DEFAULT_.curie('end'),
                   model_uri=DEFAULT_.end, domain=None, range=Optional[str])

slots.assembly = Slot(uri=DEFAULT_.assembly, name="assembly", curie=DEFAULT_.curie('assembly'),
                   model_uri=DEFAULT_.assembly, domain=GenomicEntity, range=str)

slots.gene_genomic_location_subject = Slot(uri=DEFAULT_.subject, name="gene genomic location_subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.gene_genomic_location_subject, domain=GeneGenomicLocation, range=Union[str, VariantId])

slots.gene_genomic_location_object = Slot(uri=DEFAULT_.object, name="gene genomic location_object", curie=DEFAULT_.curie('object'),
                   model_uri=DEFAULT_.gene_genomic_location_object, domain=GeneGenomicLocation, range=Union[str, ChromosomeId])
