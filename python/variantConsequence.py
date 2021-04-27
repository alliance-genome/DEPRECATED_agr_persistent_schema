# Auto generated from variantConsequence.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-27 10:55
# Schema: variantConsequence
#
# id: https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence
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
from . core import BiologicalSequence, GeneId, TranscriptId
from . variation import VariantId
from linkml_model.types import Float, Integer, String

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
DEFAULT_ = CurieNamespace('', 'https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/')


# Types

# Class references



@dataclass
class VariantGeneConsequence(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/VariantGeneConsequence")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantGeneConsequence"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/VariantGeneConsequence")

    subject: Union[str, VariantId] = None
    object: Union[str, GeneId] = None
    vep_consequence: Optional[Union[str, "VepConsequenceLevels"]] = None
    vep_impact: Optional[str] = None
    polyphen_score: Optional[float] = None
    polyphen_prediction: Optional[Union[str, "PolyphenPredictionLevels"]] = None
    sift_score: Optional[float] = None
    sift_prediction: Optional[Union[str, "SiftPredictionLevels"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, VariantId):
            self.subject = VariantId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.vep_consequence is not None and not isinstance(self.vep_consequence, VepConsequenceLevels):
            self.vep_consequence = VepConsequenceLevels(self.vep_consequence)

        if self.vep_impact is not None and not isinstance(self.vep_impact, str):
            self.vep_impact = str(self.vep_impact)

        if self.polyphen_score is not None and not isinstance(self.polyphen_score, float):
            self.polyphen_score = float(self.polyphen_score)

        if self.polyphen_prediction is not None and not isinstance(self.polyphen_prediction, PolyphenPredictionLevels):
            self.polyphen_prediction = PolyphenPredictionLevels(self.polyphen_prediction)

        if self.sift_score is not None and not isinstance(self.sift_score, float):
            self.sift_score = float(self.sift_score)

        if self.sift_prediction is not None and not isinstance(self.sift_prediction, SiftPredictionLevels):
            self.sift_prediction = SiftPredictionLevels(self.sift_prediction)

        super().__post_init__(**kwargs)


@dataclass
class VariantTranscriptConsequence(YAMLRoot):
    """
    Class for transcript-level VEP results
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/VariantTranscriptConsequence")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "VariantTranscriptConsequence"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/VariantTranscriptConsequence")

    subject: Union[str, VariantId] = None
    object: Union[str, TranscriptId] = None
    vep_consequence: Optional[Union[str, "VepConsequenceLevels"]] = None
    vep_impact: Optional[str] = None
    polyphen_score: Optional[float] = None
    polyphen_prediction: Optional[Union[str, "PolyphenPredictionLevels"]] = None
    sift_score: Optional[float] = None
    sift_prediction: Optional[Union[str, "SiftPredictionLevels"]] = None
    amino_acid_reference: Optional[Union[str, BiologicalSequence]] = None
    amino_acid_variant: Optional[Union[str, BiologicalSequence]] = None
    codon_reference: Optional[str] = None
    codon_variant: Optional[str] = None
    cdna_start: Optional[int] = None
    cdna_end: Optional[int] = None
    cds_start: Optional[int] = None
    cds_end: Optional[int] = None
    protein_start: Optional[int] = None
    protein_end: Optional[int] = None
    hgvs_protein_nomenclature: Optional[str] = None
    hgvs_coding_nomenclature: Optional[str] = None
    cnda_end: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, VariantId):
            self.subject = VariantId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)

        if self.vep_consequence is not None and not isinstance(self.vep_consequence, VepConsequenceLevels):
            self.vep_consequence = VepConsequenceLevels(self.vep_consequence)

        if self.vep_impact is not None and not isinstance(self.vep_impact, str):
            self.vep_impact = str(self.vep_impact)

        if self.polyphen_score is not None and not isinstance(self.polyphen_score, float):
            self.polyphen_score = float(self.polyphen_score)

        if self.polyphen_prediction is not None and not isinstance(self.polyphen_prediction, PolyphenPredictionLevels):
            self.polyphen_prediction = PolyphenPredictionLevels(self.polyphen_prediction)

        if self.sift_score is not None and not isinstance(self.sift_score, float):
            self.sift_score = float(self.sift_score)

        if self.sift_prediction is not None and not isinstance(self.sift_prediction, SiftPredictionLevels):
            self.sift_prediction = SiftPredictionLevels(self.sift_prediction)

        if self.amino_acid_reference is not None and not isinstance(self.amino_acid_reference, BiologicalSequence):
            self.amino_acid_reference = BiologicalSequence(self.amino_acid_reference)

        if self.amino_acid_variant is not None and not isinstance(self.amino_acid_variant, BiologicalSequence):
            self.amino_acid_variant = BiologicalSequence(self.amino_acid_variant)

        if self.codon_reference is not None and not isinstance(self.codon_reference, str):
            self.codon_reference = str(self.codon_reference)

        if self.codon_variant is not None and not isinstance(self.codon_variant, str):
            self.codon_variant = str(self.codon_variant)

        if self.cdna_start is not None and not isinstance(self.cdna_start, int):
            self.cdna_start = int(self.cdna_start)

        if self.cdna_end is not None and not isinstance(self.cdna_end, int):
            self.cdna_end = int(self.cdna_end)

        if self.cds_start is not None and not isinstance(self.cds_start, int):
            self.cds_start = int(self.cds_start)

        if self.cds_end is not None and not isinstance(self.cds_end, int):
            self.cds_end = int(self.cds_end)

        if self.protein_start is not None and not isinstance(self.protein_start, int):
            self.protein_start = int(self.protein_start)

        if self.protein_end is not None and not isinstance(self.protein_end, int):
            self.protein_end = int(self.protein_end)

        if self.hgvs_protein_nomenclature is not None and not isinstance(self.hgvs_protein_nomenclature, str):
            self.hgvs_protein_nomenclature = str(self.hgvs_protein_nomenclature)

        if self.hgvs_coding_nomenclature is not None and not isinstance(self.hgvs_coding_nomenclature, str):
            self.hgvs_coding_nomenclature = str(self.hgvs_coding_nomenclature)

        if self.cnda_end is not None and not isinstance(self.cnda_end, str):
            self.cnda_end = str(self.cnda_end)

        super().__post_init__(**kwargs)


# Enumerations
class VepConsequenceLevels(EnumDefinitionImpl):

    high = PermissibleValue(text="high")
    moderate = PermissibleValue(text="moderate")
    low = PermissibleValue(text="low")
    modifier = PermissibleValue(text="modifier")

    _defn = EnumDefinition(
        name="VepConsequenceLevels",
    )

class SiftPredictionLevels(EnumDefinitionImpl):

    deleterious = PermissibleValue(text="deleterious")
    tolerated = PermissibleValue(text="tolerated")

    _defn = EnumDefinition(
        name="SiftPredictionLevels",
    )

class PolyphenPredictionLevels(EnumDefinitionImpl):

    possibly_damaging = PermissibleValue(text="possibly_damaging")
    probably_damaging = PermissibleValue(text="probably_damaging")
    benign = PermissibleValue(text="benign")

    _defn = EnumDefinition(
        name="PolyphenPredictionLevels",
    )

# Slots
class slots:
    pass

slots.vep_impact = Slot(uri=DEFAULT_.vep_impact, name="vep_impact", curie=DEFAULT_.curie('vep_impact'),
                   model_uri=DEFAULT_.vep_impact, domain=None, range=Optional[str])

slots.vep_consequence = Slot(uri=DEFAULT_.vep_consequence, name="vep_consequence", curie=DEFAULT_.curie('vep_consequence'),
                   model_uri=DEFAULT_.vep_consequence, domain=None, range=Optional[Union[str, "VepConsequenceLevels"]])

slots.polyphen_score = Slot(uri=DEFAULT_.polyphen_score, name="polyphen_score", curie=DEFAULT_.curie('polyphen_score'),
                   model_uri=DEFAULT_.polyphen_score, domain=None, range=Optional[float])

slots.polyphen_prediction = Slot(uri=DEFAULT_.polyphen_prediction, name="polyphen_prediction", curie=DEFAULT_.curie('polyphen_prediction'),
                   model_uri=DEFAULT_.polyphen_prediction, domain=None, range=Optional[Union[str, "PolyphenPredictionLevels"]])

slots.sift_score = Slot(uri=DEFAULT_.sift_score, name="sift_score", curie=DEFAULT_.curie('sift_score'),
                   model_uri=DEFAULT_.sift_score, domain=None, range=Optional[float])

slots.sift_prediction = Slot(uri=DEFAULT_.sift_prediction, name="sift_prediction", curie=DEFAULT_.curie('sift_prediction'),
                   model_uri=DEFAULT_.sift_prediction, domain=None, range=Optional[Union[str, "SiftPredictionLevels"]])

slots.amino_acid_reference = Slot(uri=DEFAULT_.amino_acid_reference, name="amino_acid_reference", curie=DEFAULT_.curie('amino_acid_reference'),
                   model_uri=DEFAULT_.amino_acid_reference, domain=VariantTranscriptConsequence, range=Optional[Union[str, BiologicalSequence]])

slots.amino_acid_variant = Slot(uri=DEFAULT_.amino_acid_variant, name="amino_acid_variant", curie=DEFAULT_.curie('amino_acid_variant'),
                   model_uri=DEFAULT_.amino_acid_variant, domain=VariantTranscriptConsequence, range=Optional[Union[str, BiologicalSequence]])

slots.codon_reference = Slot(uri=DEFAULT_.codon_reference, name="codon_reference", curie=DEFAULT_.curie('codon_reference'),
                   model_uri=DEFAULT_.codon_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.codon_variant = Slot(uri=DEFAULT_.codon_variant, name="codon_variant", curie=DEFAULT_.curie('codon_variant'),
                   model_uri=DEFAULT_.codon_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.cdna_start = Slot(uri=DEFAULT_.cdna_start, name="cdna_start", curie=DEFAULT_.curie('cdna_start'),
                   model_uri=DEFAULT_.cdna_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cdna_end = Slot(uri=DEFAULT_.cdna_end, name="cdna_end", curie=DEFAULT_.curie('cdna_end'),
                   model_uri=DEFAULT_.cdna_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cds_start = Slot(uri=DEFAULT_.cds_start, name="cds_start", curie=DEFAULT_.curie('cds_start'),
                   model_uri=DEFAULT_.cds_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cds_end = Slot(uri=DEFAULT_.cds_end, name="cds_end", curie=DEFAULT_.curie('cds_end'),
                   model_uri=DEFAULT_.cds_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.protein_start = Slot(uri=DEFAULT_.protein_start, name="protein_start", curie=DEFAULT_.curie('protein_start'),
                   model_uri=DEFAULT_.protein_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.protein_end = Slot(uri=DEFAULT_.protein_end, name="protein_end", curie=DEFAULT_.curie('protein_end'),
                   model_uri=DEFAULT_.protein_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.hgvs_protein_nomenclature = Slot(uri=DEFAULT_.hgvs_protein_nomenclature, name="hgvs_protein_nomenclature", curie=DEFAULT_.curie('hgvs_protein_nomenclature'),
                   model_uri=DEFAULT_.hgvs_protein_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.hgvs_coding_nomenclature = Slot(uri=DEFAULT_.hgvs_coding_nomenclature, name="hgvs_coding_nomenclature", curie=DEFAULT_.curie('hgvs_coding_nomenclature'),
                   model_uri=DEFAULT_.hgvs_coding_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.cnda_end = Slot(uri=DEFAULT_.cnda_end, name="cnda_end", curie=DEFAULT_.curie('cnda_end'),
                   model_uri=DEFAULT_.cnda_end, domain=None, range=Optional[str])

slots.VariantGeneConsequence_subject = Slot(uri=DEFAULT_.subject, name="VariantGeneConsequence_subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.VariantGeneConsequence_subject, domain=VariantGeneConsequence, range=Union[str, VariantId])

slots.VariantGeneConsequence_object = Slot(uri=DEFAULT_.object, name="VariantGeneConsequence_object", curie=DEFAULT_.curie('object'),
                   model_uri=DEFAULT_.VariantGeneConsequence_object, domain=VariantGeneConsequence, range=Union[str, GeneId])

slots.VariantTranscriptConsequence_subject = Slot(uri=DEFAULT_.subject, name="VariantTranscriptConsequence_subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_subject, domain=VariantTranscriptConsequence, range=Union[str, VariantId])

slots.VariantTranscriptConsequence_object = Slot(uri=DEFAULT_.object, name="VariantTranscriptConsequence_object", curie=DEFAULT_.curie('object'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_object, domain=VariantTranscriptConsequence, range=Union[str, TranscriptId])

slots.VariantTranscriptConsequence_amino_acid_reference = Slot(uri=DEFAULT_.amino_acid_reference, name="VariantTranscriptConsequence_amino_acid_reference", curie=DEFAULT_.curie('amino_acid_reference'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_amino_acid_reference, domain=VariantTranscriptConsequence, range=Optional[Union[str, BiologicalSequence]])

slots.VariantTranscriptConsequence_amino_acid_variant = Slot(uri=DEFAULT_.amino_acid_variant, name="VariantTranscriptConsequence_amino_acid_variant", curie=DEFAULT_.curie('amino_acid_variant'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_amino_acid_variant, domain=VariantTranscriptConsequence, range=Optional[Union[str, BiologicalSequence]])

slots.VariantTranscriptConsequence_codon_reference = Slot(uri=DEFAULT_.codon_reference, name="VariantTranscriptConsequence_codon_reference", curie=DEFAULT_.curie('codon_reference'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_codon_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_codon_variant = Slot(uri=DEFAULT_.codon_variant, name="VariantTranscriptConsequence_codon_variant", curie=DEFAULT_.curie('codon_variant'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_codon_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_cdna_start = Slot(uri=DEFAULT_.cdna_start, name="VariantTranscriptConsequence_cdna_start", curie=DEFAULT_.curie('cdna_start'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_cdna_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_cnda_end = Slot(uri=DEFAULT_.cnda_end, name="VariantTranscriptConsequence_cnda_end", curie=DEFAULT_.curie('cnda_end'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_cnda_end, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_cds_start = Slot(uri=DEFAULT_.cds_start, name="VariantTranscriptConsequence_cds_start", curie=DEFAULT_.curie('cds_start'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_cds_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_cds_end = Slot(uri=DEFAULT_.cds_end, name="VariantTranscriptConsequence_cds_end", curie=DEFAULT_.curie('cds_end'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_cds_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_protein_start = Slot(uri=DEFAULT_.protein_start, name="VariantTranscriptConsequence_protein_start", curie=DEFAULT_.curie('protein_start'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_protein_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_protein_end = Slot(uri=DEFAULT_.protein_end, name="VariantTranscriptConsequence_protein_end", curie=DEFAULT_.curie('protein_end'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_protein_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.VariantTranscriptConsequence_hgvs_protein_nomenclature = Slot(uri=DEFAULT_.hgvs_protein_nomenclature, name="VariantTranscriptConsequence_hgvs_protein_nomenclature", curie=DEFAULT_.curie('hgvs_protein_nomenclature'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_hgvs_protein_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.VariantTranscriptConsequence_hgvs_coding_nomenclature = Slot(uri=DEFAULT_.hgvs_coding_nomenclature, name="VariantTranscriptConsequence_hgvs_coding_nomenclature", curie=DEFAULT_.curie('hgvs_coding_nomenclature'),
                   model_uri=DEFAULT_.VariantTranscriptConsequence_hgvs_coding_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])
