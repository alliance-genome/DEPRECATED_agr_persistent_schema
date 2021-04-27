# Auto generated from crossReference.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-27 08:49
# Schema: crossReference
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/crossReference
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
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/crossReference/')


# Types

# Class references
class CrossReferenceCrossReferenceId(extended_str):
    pass


@dataclass
class CrossReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/crossReference/CrossReference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "cross reference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/crossReference/CrossReference")

    cross_reference_id: Union[str, CrossReferenceCrossReferenceId] = None
    page_areas: Union[str, List[str]] = None
    display_name: str = None
    prefix: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.cross_reference_id is None:
            raise ValueError("cross_reference_id must be supplied")
        if not isinstance(self.cross_reference_id, CrossReferenceCrossReferenceId):
            self.cross_reference_id = CrossReferenceCrossReferenceId(self.cross_reference_id)

        if self.page_areas is None:
            raise ValueError("page_areas must be supplied")
        elif not isinstance(self.page_areas, list):
            self.page_areas = [self.page_areas]
        elif len(self.page_areas) == 0:
            raise ValueError(f"page_areas must be a non-empty list")
        self.page_areas = [v if isinstance(v, str) else str(v) for v in self.page_areas]

        if self.display_name is None:
            raise ValueError("display_name must be supplied")
        if not isinstance(self.display_name, str):
            self.display_name = str(self.display_name)

        if self.prefix is None:
            raise ValueError("prefix must be supplied")
        if not isinstance(self.prefix, str):
            self.prefix = str(self.prefix)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.prefix = Slot(uri=DEFAULT_.prefix, name="prefix", curie=DEFAULT_.curie('prefix'),
                   model_uri=DEFAULT_.prefix, domain=None, range=str)

slots.page_areas = Slot(uri=DEFAULT_.page_areas, name="page areas", curie=DEFAULT_.curie('page_areas'),
                   model_uri=DEFAULT_.page_areas, domain=None, range=Union[str, List[str]])

slots.display_name = Slot(uri=DEFAULT_.display_name, name="display name", curie=DEFAULT_.curie('display_name'),
                   model_uri=DEFAULT_.display_name, domain=None, range=str)

slots.cross_reference_id = Slot(uri=DEFAULT_.cross_reference_id, name="cross reference id", curie=DEFAULT_.curie('cross_reference_id'),
                   model_uri=DEFAULT_.cross_reference_id, domain=None, range=URIRef)
