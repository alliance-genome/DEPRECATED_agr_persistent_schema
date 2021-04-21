# Auto generated from variantGenomicLocation.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-21 15:41
# Schema: Alliance-Schema-Prototype-Variation
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantGenomicLocation
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
from . core import NamedThing
from . genomic import AssemblyId, ChromosomeId
from . variation import VariantId
from linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantGenomicLocation/')


# Types

# Class references



@dataclass
class VariantToChromosome(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantGenomicLocation/VariantToChromosome")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "variant to chromosome"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantGenomicLocation/VariantToChromosome")

    variantId: Union[str, VariantId] = None
    chromosomeId: Union[str, ChromosomeId] = None
    assemblyId: Union[str, AssemblyId] = None
    start: Optional[str] = None
    end: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.variantId is None:
            raise ValueError("variantId must be supplied")
        if not isinstance(self.variantId, VariantId):
            self.variantId = VariantId(self.variantId)

        if self.chromosomeId is None:
            raise ValueError("chromosomeId must be supplied")
        if not isinstance(self.chromosomeId, ChromosomeId):
            self.chromosomeId = ChromosomeId(self.chromosomeId)

        if self.assemblyId is None:
            raise ValueError("assemblyId must be supplied")
        if not isinstance(self.assemblyId, AssemblyId):
            self.assemblyId = AssemblyId(self.assemblyId)

        if self.start is not None and not isinstance(self.start, str):
            self.start = str(self.start)

        if self.end is not None and not isinstance(self.end, str):
            self.end = str(self.end)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.located_on = Slot(uri=DEFAULT_.located_on, name="located on", curie=DEFAULT_.curie('located_on'),
                   model_uri=DEFAULT_.located_on, domain=NamedThing, range=Optional[Union[str, ChromosomeId]])
