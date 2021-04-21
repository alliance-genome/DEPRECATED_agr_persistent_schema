# Auto generated from informationContentEntity.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-21 15:51
# Schema: informationContentEntity
#
# id: https://github.com/alliance-genome/agr_persistent_schema/informationContentEntity
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
from . crossReference import CrossReferenceCrossReferenceId
from . reference import ReferenceId
from linkml.utils.metamodelcore import XSDDate
from linkml_model.types import Date, String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
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

# Class references



@dataclass
class InformationContentEntity(YAMLRoot):
    """
    a piece of information that typically describes some topic of discourse or is used as support. Precedence of
    identifiers for references is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.InformationContentEntity
    class_class_curie: ClassVar[str] = "alliance:InformationContentEntity"
    class_name: ClassVar[str] = "information content entity"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.InformationContentEntity

    creation_date: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        super().__post_init__(**kwargs)


@dataclass
class AuthorReference(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALLIANCE.AuthorReference
    class_class_curie: ClassVar[str] = "alliance:AuthorReference"
    class_name: ClassVar[str] = "author reference"
    class_model_uri: ClassVar[URIRef] = ALLIANCE.AuthorReference

    corresponding_author: Optional[Union[dict, InformationContentEntity]] = None
    first_name: Optional[Union[dict, InformationContentEntity]] = None
    middle_names: Optional[Union[dict, InformationContentEntity]] = None
    last_name: Optional[Union[dict, InformationContentEntity]] = None
    initials: Optional[Union[dict, InformationContentEntity]] = None
    cross_references: Optional[Union[Union[str, CrossReferenceCrossReferenceId], List[Union[str, CrossReferenceCrossReferenceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.corresponding_author is not None and not isinstance(self.corresponding_author, InformationContentEntity):
            self.corresponding_author = InformationContentEntity(**self.corresponding_author)

        if self.first_name is not None and not isinstance(self.first_name, InformationContentEntity):
            self.first_name = InformationContentEntity(**self.first_name)

        if self.middle_names is not None and not isinstance(self.middle_names, InformationContentEntity):
            self.middle_names = InformationContentEntity(**self.middle_names)

        if self.last_name is not None and not isinstance(self.last_name, InformationContentEntity):
            self.last_name = InformationContentEntity(**self.last_name)

        if self.initials is not None and not isinstance(self.initials, InformationContentEntity):
            self.initials = InformationContentEntity(**self.initials)

        if self.cross_references is None:
            self.cross_references = []
        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references]
        self.cross_references = [v if isinstance(v, CrossReferenceCrossReferenceId) else CrossReferenceCrossReferenceId(v) for v in self.cross_references]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.creation_date = Slot(uri=ALLIANCE.creation_date, name="creation date", curie=ALLIANCE.curie('creation_date'),
                   model_uri=ALLIANCE.creation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.summary = Slot(uri=ALLIANCE.summary, name="summary", curie=ALLIANCE.curie('summary'),
                   model_uri=ALLIANCE.summary, domain=InformationContentEntity, range=Optional[str])

slots.copyright_date = Slot(uri=ALLIANCE.copyright_date, name="copyright date", curie=ALLIANCE.curie('copyright_date'),
                   model_uri=ALLIANCE.copyright_date, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.references = Slot(uri=ALLIANCE.references, name="references", curie=ALLIANCE.curie('references'),
                   model_uri=ALLIANCE.references, domain=NamedThing, range=Optional[Union[Union[str, ReferenceId], List[Union[str, ReferenceId]]]])

slots.authors = Slot(uri=ALLIANCE.authors, name="authors", curie=ALLIANCE.curie('authors'),
                   model_uri=ALLIANCE.authors, domain=InformationContentEntity, range=Optional[Union[Union[dict, "AuthorReference"], List[Union[dict, "AuthorReference"]]]])

slots.corresponding_author = Slot(uri=ALLIANCE.corresponding_author, name="corresponding author", curie=ALLIANCE.curie('corresponding_author'),
                   model_uri=ALLIANCE.corresponding_author, domain=InformationContentEntity, range=Optional[Union[dict, "InformationContentEntity"]])

slots.first_name = Slot(uri=ALLIANCE.first_name, name="first name", curie=ALLIANCE.curie('first_name'),
                   model_uri=ALLIANCE.first_name, domain=InformationContentEntity, range=Optional[Union[dict, "InformationContentEntity"]])

slots.middle_names = Slot(uri=ALLIANCE.middle_names, name="middle names", curie=ALLIANCE.curie('middle_names'),
                   model_uri=ALLIANCE.middle_names, domain=InformationContentEntity, range=Optional[Union[dict, "InformationContentEntity"]])

slots.last_name = Slot(uri=FOAF.familyName, name="last name", curie=FOAF.curie('familyName'),
                   model_uri=ALLIANCE.last_name, domain=InformationContentEntity, range=Optional[Union[dict, "InformationContentEntity"]])

slots.initials = Slot(uri=ALLIANCE.initials, name="initials", curie=ALLIANCE.curie('initials'),
                   model_uri=ALLIANCE.initials, domain=InformationContentEntity, range=Optional[Union[dict, "InformationContentEntity"]])

slots.title = Slot(uri=ALLIANCE.title, name="title", curie=ALLIANCE.curie('title'),
                   model_uri=ALLIANCE.title, domain=InformationContentEntity, range=Optional[str])

slots.volumes = Slot(uri=ALLIANCE.volumes, name="volumes", curie=ALLIANCE.curie('volumes'),
                   model_uri=ALLIANCE.volumes, domain=InformationContentEntity, range=Optional[str])

slots.publisher = Slot(uri=ALLIANCE.publisher, name="publisher", curie=ALLIANCE.curie('publisher'),
                   model_uri=ALLIANCE.publisher, domain=InformationContentEntity, range=Optional[Union[dict, "InformationContentEntity"]])

slots.address = Slot(uri=ALLIANCE.address, name="address", curie=ALLIANCE.curie('address'),
                   model_uri=ALLIANCE.address, domain=None, range=Optional[str])
