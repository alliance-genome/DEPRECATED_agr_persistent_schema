# Auto generated from reference.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-21 16:17
# Schema: reference
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/reference
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
from . core import Id
from . crossReference import CrossReferenceCrossReferenceId
from . informationContentEntity import AuthorReference, InformationContentEntity
from linkml.utils.metamodelcore import URIorCURIE, XSDDate
from linkml_model.types import Date, String, Uriorcurie

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DOI = CurieNamespace('DOI', 'http://identifiers.org/doi/')
FB = CurieNamespace('FB', 'http://identifiers.org/fb/')
MGI = CurieNamespace('MGI', 'http://identifiers.org/mgi/')
NLMID = CurieNamespace('NLMID', 'https://www.ncbi.nlm.nih.gov/nlmcatalog/?term=')
PMC = CurieNamespace('PMC', 'http://identifiers.org/pmc/')
PMID = CurieNamespace('PMID', 'http://www.ncbi.nlm.nih.gov/pubmed/')
RGD = CurieNamespace('RGD', 'http://identifiers.org/rgd/')
SGD = CurieNamespace('SGD', 'http://identifiers.org/sgd/')
WB = CurieNamespace('WB', 'http://identifiers.org/wb/')
ZFIN = CurieNamespace('ZFIN', 'http://identifiers.org/zfin/')
ALLIANCE = CurieNamespace('alliance', 'http://alliancegenome.org')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/reference/')


# Types

# Class references
class ReferenceId(URIorCURIE):
    pass


@dataclass
class Reference(InformationContentEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/reference/Reference")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "reference"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/reference/Reference")

    id: Union[str, ReferenceId] = None
    reference_id: Optional[str] = None
    title: Optional[str] = None
    alliance_category: Optional[str] = None
    date_published: Optional[Union[str, XSDDate]] = None
    year_published: Optional[str] = None
    month_published: Optional[str] = None
    day_published: Optional[str] = None
    date_arrived_in_PubMed: Optional[Union[str, XSDDate]] = None
    date_last_modified_in_PubMed: Optional[Union[str, XSDDate]] = None
    date_last_modified: Optional[Union[str, XSDDate]] = None
    volume: Optional[str] = None
    pages: Optional[Union[str, List[str]]] = empty_list()
    abstract: Optional[str] = None
    citation: Optional[str] = None
    PubMed_type: Optional[str] = None
    issue_name: Optional[str] = None
    issue_date: Optional[Union[str, XSDDate]] = None
    mod_reference_types: Optional[Union[str, List[str]]] = empty_list()
    authors: Optional[Union[Union[dict, AuthorReference], List[Union[dict, AuthorReference]]]] = empty_list()
    tags: Optional[Union[str, List[str]]] = empty_list()
    topics: Optional[Union[str, URIorCURIE]] = None
    cross_references: Optional[Union[Union[str, CrossReferenceCrossReferenceId], List[Union[str, CrossReferenceCrossReferenceId]]]] = empty_list()
    publisher: Optional[Union[dict, InformationContentEntity]] = None
    keywords: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError("id must be supplied")
        if not isinstance(self.id, ReferenceId):
            self.id = ReferenceId(self.id)

        if self.reference_id is not None and not isinstance(self.reference_id, str):
            self.reference_id = str(self.reference_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.alliance_category is not None and not isinstance(self.alliance_category, str):
            self.alliance_category = str(self.alliance_category)

        if self.date_published is not None and not isinstance(self.date_published, XSDDate):
            self.date_published = XSDDate(self.date_published)

        if self.year_published is not None and not isinstance(self.year_published, str):
            self.year_published = str(self.year_published)

        if self.month_published is not None and not isinstance(self.month_published, str):
            self.month_published = str(self.month_published)

        if self.day_published is not None and not isinstance(self.day_published, str):
            self.day_published = str(self.day_published)

        if self.date_arrived_in_PubMed is not None and not isinstance(self.date_arrived_in_PubMed, XSDDate):
            self.date_arrived_in_PubMed = XSDDate(self.date_arrived_in_PubMed)

        if self.date_last_modified_in_PubMed is not None and not isinstance(self.date_last_modified_in_PubMed, XSDDate):
            self.date_last_modified_in_PubMed = XSDDate(self.date_last_modified_in_PubMed)

        if self.date_last_modified is not None and not isinstance(self.date_last_modified, XSDDate):
            self.date_last_modified = XSDDate(self.date_last_modified)

        if self.volume is not None and not isinstance(self.volume, str):
            self.volume = str(self.volume)

        if self.pages is None:
            self.pages = []
        if not isinstance(self.pages, list):
            self.pages = [self.pages]
        self.pages = [v if isinstance(v, str) else str(v) for v in self.pages]

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.citation is not None and not isinstance(self.citation, str):
            self.citation = str(self.citation)

        if self.PubMed_type is not None and not isinstance(self.PubMed_type, str):
            self.PubMed_type = str(self.PubMed_type)

        if self.issue_name is not None and not isinstance(self.issue_name, str):
            self.issue_name = str(self.issue_name)

        if self.issue_date is not None and not isinstance(self.issue_date, XSDDate):
            self.issue_date = XSDDate(self.issue_date)

        if self.mod_reference_types is None:
            self.mod_reference_types = []
        if not isinstance(self.mod_reference_types, list):
            self.mod_reference_types = [self.mod_reference_types]
        self.mod_reference_types = [v if isinstance(v, str) else str(v) for v in self.mod_reference_types]

        if self.authors is None:
            self.authors = []
        if not isinstance(self.authors, list):
            self.authors = [self.authors]
        self.authors = [v if isinstance(v, AuthorReference) else AuthorReference(**v) for v in self.authors]

        if self.tags is None:
            self.tags = []
        if not isinstance(self.tags, list):
            self.tags = [self.tags]
        self.tags = [v if isinstance(v, str) else str(v) for v in self.tags]

        if self.topics is not None and not isinstance(self.topics, URIorCURIE):
            self.topics = URIorCURIE(self.topics)

        if self.cross_references is None:
            self.cross_references = []
        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references]
        self.cross_references = [v if isinstance(v, CrossReferenceCrossReferenceId) else CrossReferenceCrossReferenceId(v) for v in self.cross_references]

        if self.publisher is not None and not isinstance(self.publisher, InformationContentEntity):
            self.publisher = InformationContentEntity(**self.publisher)

        if self.keywords is None:
            self.keywords = []
        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords]
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.reference_id = Slot(uri=DEFAULT_.reference_id, name="reference id", curie=DEFAULT_.curie('reference_id'),
                   model_uri=DEFAULT_.reference_id, domain=Reference, range=Optional[str])

slots.topics = Slot(uri=DEFAULT_.topics, name="topics", curie=DEFAULT_.curie('topics'),
                   model_uri=DEFAULT_.topics, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.PubMed_type = Slot(uri=DEFAULT_.PubMed_type, name="PubMed type", curie=DEFAULT_.curie('PubMed_type'),
                   model_uri=DEFAULT_.PubMed_type, domain=InformationContentEntity, range=Optional[str])

slots.date_published = Slot(uri=DEFAULT_.date_published, name="date published", curie=DEFAULT_.curie('date_published'),
                   model_uri=DEFAULT_.date_published, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.date_last_modified_in_PubMed = Slot(uri=DEFAULT_.date_last_modified_in_PubMed, name="date last modified in PubMed", curie=DEFAULT_.curie('date_last_modified_in_PubMed'),
                   model_uri=DEFAULT_.date_last_modified_in_PubMed, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.date_last_modified = Slot(uri=DEFAULT_.date_last_modified, name="date last modified", curie=DEFAULT_.curie('date_last_modified'),
                   model_uri=DEFAULT_.date_last_modified, domain=None, range=Optional[Union[str, XSDDate]])

slots.year_published = Slot(uri=DEFAULT_.year_published, name="year published", curie=DEFAULT_.curie('year_published'),
                   model_uri=DEFAULT_.year_published, domain=InformationContentEntity, range=Optional[str])

slots.month_published = Slot(uri=DEFAULT_.month_published, name="month published", curie=DEFAULT_.curie('month_published'),
                   model_uri=DEFAULT_.month_published, domain=InformationContentEntity, range=Optional[str])

slots.day_published = Slot(uri=DEFAULT_.day_published, name="day published", curie=DEFAULT_.curie('day_published'),
                   model_uri=DEFAULT_.day_published, domain=InformationContentEntity, range=Optional[str])

slots.date_arrived_in_PubMed = Slot(uri=DEFAULT_.date_arrived_in_PubMed, name="date arrived in PubMed", curie=DEFAULT_.curie('date_arrived_in_PubMed'),
                   model_uri=DEFAULT_.date_arrived_in_PubMed, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.mod_reference_types = Slot(uri=DEFAULT_.mod_reference_types, name="mod reference types", curie=DEFAULT_.curie('mod_reference_types'),
                   model_uri=DEFAULT_.mod_reference_types, domain=None, range=Optional[Union[str, List[str]]])

slots.tags = Slot(uri=DEFAULT_.tags, name="tags", curie=DEFAULT_.curie('tags'),
                   model_uri=DEFAULT_.tags, domain=None, range=Optional[Union[str, List[str]]])

slots.issue_date = Slot(uri=DEFAULT_.issue_date, name="issue date", curie=DEFAULT_.curie('issue_date'),
                   model_uri=DEFAULT_.issue_date, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.last_modified = Slot(uri=DEFAULT_.last_modified, name="last modified", curie=DEFAULT_.curie('last_modified'),
                   model_uri=DEFAULT_.last_modified, domain=InformationContentEntity, range=Optional[Union[str, XSDDate]])

slots.volume = Slot(uri=DEFAULT_.volume, name="volume", curie=DEFAULT_.curie('volume'),
                   model_uri=DEFAULT_.volume, domain=InformationContentEntity, range=Optional[str])

slots.pages = Slot(uri=DEFAULT_.pages, name="pages", curie=DEFAULT_.curie('pages'),
                   model_uri=DEFAULT_.pages, domain=InformationContentEntity, range=Optional[Union[str, List[str]]])

slots.abstract = Slot(uri=DEFAULT_.abstract, name="abstract", curie=DEFAULT_.curie('abstract'),
                   model_uri=DEFAULT_.abstract, domain=Reference, range=Optional[str])

slots.citation = Slot(uri=DEFAULT_.citation, name="citation", curie=DEFAULT_.curie('citation'),
                   model_uri=DEFAULT_.citation, domain=Reference, range=Optional[str])

slots.issue_name = Slot(uri=DEFAULT_.issue_name, name="issue name", curie=DEFAULT_.curie('issue_name'),
                   model_uri=DEFAULT_.issue_name, domain=Reference, range=Optional[str])

slots.alliance_category = Slot(uri=DEFAULT_.alliance_category, name="alliance category", curie=DEFAULT_.curie('alliance_category'),
                   model_uri=DEFAULT_.alliance_category, domain=Reference, range=Optional[str])

slots.keywords = Slot(uri=DEFAULT_.keywords, name="keywords", curie=DEFAULT_.curie('keywords'),
                   model_uri=DEFAULT_.keywords, domain=InformationContentEntity, range=Optional[Union[str, List[str]]])

slots.reference_id = Slot(uri=DEFAULT_.id, name="reference_id", curie=DEFAULT_.curie('id'),
                   model_uri=DEFAULT_.reference_id, domain=Reference, range=Union[str, ReferenceId])
