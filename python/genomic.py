# Auto generated from genomic.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-21 15:40
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
from . core import GeneId, NamedThing, NamedThingId, TranscriptId
from . variation import VariantId
from linkml.utils.metamodelcore import URIorCURIE
from linkml_model.types import String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/')


# Types

# Class references
class ChromosomeId(NamedThingId):
    pass


class AssemblyId(NamedThingId):
    pass


@dataclass
class Chromosome(NamedThing):
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
class Assembly(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/Assembly")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "assembly"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/genomic/Assembly")

    id: Union[str, AssemblyId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, AssemblyId):
            self.id = AssemblyId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.start = Slot(uri=DEFAULT_.start, name="start", curie=DEFAULT_.curie('start'),
                   model_uri=DEFAULT_.start, domain=None, range=Optional[str])

slots.end = Slot(uri=DEFAULT_.end, name="end", curie=DEFAULT_.curie('end'),
                   model_uri=DEFAULT_.end, domain=None, range=Optional[str])

slots.variantId = Slot(uri=DEFAULT_.variantId, name="variantId", curie=DEFAULT_.curie('variantId'),
                   model_uri=DEFAULT_.variantId, domain=None, range=Union[str, VariantId])

slots.geneId = Slot(uri=DEFAULT_.geneId, name="geneId", curie=DEFAULT_.curie('geneId'),
                   model_uri=DEFAULT_.geneId, domain=None, range=Union[str, GeneId])

slots.chromosomeId = Slot(uri=DEFAULT_.chromosomeId, name="chromosomeId", curie=DEFAULT_.curie('chromosomeId'),
                   model_uri=DEFAULT_.chromosomeId, domain=None, range=Union[str, ChromosomeId])

slots.transcriptId = Slot(uri=DEFAULT_.transcriptId, name="transcriptId", curie=DEFAULT_.curie('transcriptId'),
                   model_uri=DEFAULT_.transcriptId, domain=None, range=Union[str, TranscriptId])

slots.assemblyId = Slot(uri=DEFAULT_.assemblyId, name="assemblyId", curie=DEFAULT_.curie('assemblyId'),
                   model_uri=DEFAULT_.assemblyId, domain=None, range=Union[str, AssemblyId])
