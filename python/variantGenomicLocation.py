# Auto generated from variantGenomicLocation.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-14 16:32
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
from . genomic import Assembly, Chromosome
from linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantGenomicLocation/')


# Types

# Class references



@dataclass
class VariantToChromosomeAssociation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantGenomicLocation/VariantToChromosomeAssociation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "variant to chromosome association"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantGenomicLocation/VariantToChromosomeAssociation")

    subject: Union[dict, NamedThing] = None
    predicate: str = None
    object: Union[dict, NamedThing] = None
    has_chromosome: Optional[Union[dict, Chromosome]] = None
    has_assembly: Optional[Union[dict, Assembly]] = None
    start: Optional[str] = None
    end: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, NamedThing):
            self.subject = NamedThing()

        if self.predicate is None:
            raise ValueError("predicate must be supplied")
        if not isinstance(self.predicate, str):
            self.predicate = str(self.predicate)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, NamedThing):
            self.object = NamedThing()

        if self.has_chromosome is not None and not isinstance(self.has_chromosome, Chromosome):
            self.has_chromosome = Chromosome()

        if self.has_assembly is not None and not isinstance(self.has_assembly, Assembly):
            self.has_assembly = Assembly()

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
                   model_uri=DEFAULT_.located_on, domain=NamedThing, range=Optional[Union[dict, Chromosome]])

slots.has_chromosome = Slot(uri=DEFAULT_.has_chromosome, name="has chromosome", curie=DEFAULT_.curie('has_chromosome'),
                   model_uri=DEFAULT_.has_chromosome, domain=VariantToChromosomeAssociation, range=Optional[Union[dict, Chromosome]])

slots.has_assembly = Slot(uri=DEFAULT_.has_assembly, name="has assembly", curie=DEFAULT_.curie('has_assembly'),
                   model_uri=DEFAULT_.has_assembly, domain=VariantToChromosomeAssociation, range=Optional[Union[dict, Assembly]])

slots.variant_to_chromosome_association_subject = Slot(uri=DEFAULT_.subject, name="variant to chromosome association_subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.variant_to_chromosome_association_subject, domain=VariantToChromosomeAssociation, range=Union[dict, NamedThing])

slots.variant_to_chromosome_association_object = Slot(uri=DEFAULT_.object, name="variant to chromosome association_object", curie=DEFAULT_.curie('object'),
                   model_uri=DEFAULT_.variant_to_chromosome_association_object, domain=VariantToChromosomeAssociation, range=Union[dict, NamedThing])

slots.variant_to_chromosome_association_predicate = Slot(uri=DEFAULT_.predicate, name="variant to chromosome association_predicate", curie=DEFAULT_.curie('predicate'),
                   model_uri=DEFAULT_.variant_to_chromosome_association_predicate, domain=VariantToChromosomeAssociation, range=str)
