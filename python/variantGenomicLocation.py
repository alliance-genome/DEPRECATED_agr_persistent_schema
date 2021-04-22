# Auto generated from variantGenomicLocation.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-21 18:08
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
from . genomic import AssemblyId, ChromosomeId
from . variation import VariantId
from linkml_model.types import String

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
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantGenomicLocation/')


# Types

# Class references
class VariantToChromosomeVariantId(extended_str):
    pass


@dataclass
class VariantGenomicLocation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantGenomicLocation/VariantGenomicLocation")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "variant genomic location"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantGenomicLocation/VariantGenomicLocation")

    subject: Union[str, VariantId] = None
    predicate: str = None
    object: Union[str, ChromosomeId] = None
    has_assembly: Union[str, AssemblyId] = None
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

        if self.has_assembly is None:
            raise ValueError("has_assembly must be supplied")
        if not isinstance(self.has_assembly, AssemblyId):
            self.has_assembly = AssemblyId(self.has_assembly)

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
                   model_uri=DEFAULT_.located_on, domain=None, range=Optional[Union[str, ChromosomeId]])

slots.has_assembly = Slot(uri=DEFAULT_.has_assembly, name="has assembly", curie=DEFAULT_.curie('has_assembly'),
                   model_uri=DEFAULT_.has_assembly, domain=VariantGenomicLocation, range=Union[str, AssemblyId])

slots.variant_genomic_location_subject = Slot(uri=DEFAULT_.subject, name="variant genomic location_subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.variant_genomic_location_subject, domain=VariantGenomicLocation, range=Union[str, VariantId])

slots.variant_genomic_location_object = Slot(uri=DEFAULT_.object, name="variant genomic location_object", curie=DEFAULT_.curie('object'),
                   model_uri=DEFAULT_.variant_genomic_location_object, domain=VariantGenomicLocation, range=Union[str, ChromosomeId])

slots.variant_genomic_location_predicate = Slot(uri=DEFAULT_.predicate, name="variant genomic location_predicate", curie=DEFAULT_.curie('predicate'),
                   model_uri=DEFAULT_.variant_genomic_location_predicate, domain=VariantGenomicLocation, range=str)
