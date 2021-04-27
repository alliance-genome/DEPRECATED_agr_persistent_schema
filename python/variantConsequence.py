# Auto generated from variantConsequence.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-04-27 08:58
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
    class_name: ClassVar[str] = "variant gene consequence"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/VariantGeneConsequence")

    subject: Union[str, VariantId] = None
    object: Union[str, GeneId] = None
    vep_consequence: Optional[str] = None
    vep_impact: Optional[str] = None
    polyphen_score: Optional[float] = None
    polyphen_prediction: Optional[str] = None
    sift_score: Optional[float] = None
    sift_prediction: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, VariantId):
            self.subject = VariantId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

        if self.vep_consequence is not None and not isinstance(self.vep_consequence, str):
            self.vep_consequence = str(self.vep_consequence)

        if self.vep_impact is not None and not isinstance(self.vep_impact, str):
            self.vep_impact = str(self.vep_impact)

        if self.polyphen_score is not None and not isinstance(self.polyphen_score, float):
            self.polyphen_score = float(self.polyphen_score)

        if self.polyphen_prediction is not None and not isinstance(self.polyphen_prediction, str):
            self.polyphen_prediction = str(self.polyphen_prediction)

        if self.sift_score is not None and not isinstance(self.sift_score, float):
            self.sift_score = float(self.sift_score)

        if self.sift_prediction is not None and not isinstance(self.sift_prediction, str):
            self.sift_prediction = str(self.sift_prediction)

        super().__post_init__(**kwargs)


@dataclass
class VariantTranscriptConsequence(YAMLRoot):
    """
    Class for transcript-level VEP results
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/VariantTranscriptConsequence")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "variant transcript consequence"
    class_model_uri: ClassVar[URIRef] = URIRef("https://github.com/alliance-genome/agr_persistent_schema/src/schema/variantConsequence/VariantTranscriptConsequence")

    subject: Union[str, VariantId] = None
    object: Union[str, TranscriptId] = None
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
    cns_end: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is None:
            raise ValueError("subject must be supplied")
        if not isinstance(self.subject, VariantId):
            self.subject = VariantId(self.subject)

        if self.object is None:
            raise ValueError("object must be supplied")
        if not isinstance(self.object, TranscriptId):
            self.object = TranscriptId(self.object)

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

        if self.cns_end is not None and not isinstance(self.cns_end, str):
            self.cns_end = str(self.cns_end)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.vep_impact = Slot(uri=DEFAULT_.vep_impact, name="vep impact", curie=DEFAULT_.curie('vep_impact'),
                   model_uri=DEFAULT_.vep_impact, domain=VariantGeneConsequence, range=Optional[str])

slots.polyphen_score = Slot(uri=DEFAULT_.polyphen_score, name="polyphen score", curie=DEFAULT_.curie('polyphen_score'),
                   model_uri=DEFAULT_.polyphen_score, domain=VariantGeneConsequence, range=Optional[float])

slots.polyphen_prediction = Slot(uri=DEFAULT_.polyphen_prediction, name="polyphen prediction", curie=DEFAULT_.curie('polyphen_prediction'),
                   model_uri=DEFAULT_.polyphen_prediction, domain=VariantGeneConsequence, range=Optional[str])

slots.sift_score = Slot(uri=DEFAULT_.sift_score, name="sift score", curie=DEFAULT_.curie('sift_score'),
                   model_uri=DEFAULT_.sift_score, domain=VariantGeneConsequence, range=Optional[float])

slots.sift_prediction = Slot(uri=DEFAULT_.sift_prediction, name="sift prediction", curie=DEFAULT_.curie('sift_prediction'),
                   model_uri=DEFAULT_.sift_prediction, domain=VariantGeneConsequence, range=Optional[str])

slots.amino_acid_reference = Slot(uri=DEFAULT_.amino_acid_reference, name="amino acid reference", curie=DEFAULT_.curie('amino_acid_reference'),
                   model_uri=DEFAULT_.amino_acid_reference, domain=VariantTranscriptConsequence, range=Optional[Union[str, BiologicalSequence]])

slots.amino_acid_variant = Slot(uri=DEFAULT_.amino_acid_variant, name="amino acid variant", curie=DEFAULT_.curie('amino_acid_variant'),
                   model_uri=DEFAULT_.amino_acid_variant, domain=VariantTranscriptConsequence, range=Optional[Union[str, BiologicalSequence]])

slots.codon_reference = Slot(uri=DEFAULT_.codon_reference, name="codon reference", curie=DEFAULT_.curie('codon_reference'),
                   model_uri=DEFAULT_.codon_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.codon_variant = Slot(uri=DEFAULT_.codon_variant, name="codon variant", curie=DEFAULT_.curie('codon_variant'),
                   model_uri=DEFAULT_.codon_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.cdna_start = Slot(uri=DEFAULT_.cdna_start, name="cdna start", curie=DEFAULT_.curie('cdna_start'),
                   model_uri=DEFAULT_.cdna_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cdna_end = Slot(uri=DEFAULT_.cdna_end, name="cdna end", curie=DEFAULT_.curie('cdna_end'),
                   model_uri=DEFAULT_.cdna_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cds_start = Slot(uri=DEFAULT_.cds_start, name="cds start", curie=DEFAULT_.curie('cds_start'),
                   model_uri=DEFAULT_.cds_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.cds_end = Slot(uri=DEFAULT_.cds_end, name="cds end", curie=DEFAULT_.curie('cds_end'),
                   model_uri=DEFAULT_.cds_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.protein_start = Slot(uri=DEFAULT_.protein_start, name="protein start", curie=DEFAULT_.curie('protein_start'),
                   model_uri=DEFAULT_.protein_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.protein_end = Slot(uri=DEFAULT_.protein_end, name="protein end", curie=DEFAULT_.curie('protein_end'),
                   model_uri=DEFAULT_.protein_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.hgvs_protein_nomenclature = Slot(uri=DEFAULT_.hgvs_protein_nomenclature, name="hgvs protein nomenclature", curie=DEFAULT_.curie('hgvs_protein_nomenclature'),
                   model_uri=DEFAULT_.hgvs_protein_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.hgvs_coding_nomenclature = Slot(uri=DEFAULT_.hgvs_coding_nomenclature, name="hgvs coding nomenclature", curie=DEFAULT_.curie('hgvs_coding_nomenclature'),
                   model_uri=DEFAULT_.hgvs_coding_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.vep_consequence = Slot(uri=DEFAULT_.vep_consequence, name="vep consequence", curie=DEFAULT_.curie('vep_consequence'),
                   model_uri=DEFAULT_.vep_consequence, domain=None, range=Optional[str])

slots.cnda_end = Slot(uri=DEFAULT_.cnda_end, name="cnda end", curie=DEFAULT_.curie('cnda_end'),
                   model_uri=DEFAULT_.cnda_end, domain=None, range=Optional[str])

slots.cns_end = Slot(uri=DEFAULT_.cns_end, name="cns end", curie=DEFAULT_.curie('cns_end'),
                   model_uri=DEFAULT_.cns_end, domain=None, range=Optional[str])

slots.variant_gene_consequence_subject = Slot(uri=DEFAULT_.subject, name="variant gene consequence_subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.variant_gene_consequence_subject, domain=VariantGeneConsequence, range=Union[str, VariantId])

slots.variant_gene_consequence_object = Slot(uri=DEFAULT_.object, name="variant gene consequence_object", curie=DEFAULT_.curie('object'),
                   model_uri=DEFAULT_.variant_gene_consequence_object, domain=VariantGeneConsequence, range=Union[str, GeneId])

slots.variant_transcript_consequence_subject = Slot(uri=DEFAULT_.subject, name="variant transcript consequence_subject", curie=DEFAULT_.curie('subject'),
                   model_uri=DEFAULT_.variant_transcript_consequence_subject, domain=VariantTranscriptConsequence, range=Union[str, VariantId])

slots.variant_transcript_consequence_object = Slot(uri=DEFAULT_.object, name="variant transcript consequence_object", curie=DEFAULT_.curie('object'),
                   model_uri=DEFAULT_.variant_transcript_consequence_object, domain=VariantTranscriptConsequence, range=Union[str, TranscriptId])

slots.variant_transcript_consequence_amino_acid_reference = Slot(uri=DEFAULT_.amino_acid_reference, name="variant transcript consequence_amino acid reference", curie=DEFAULT_.curie('amino_acid_reference'),
                   model_uri=DEFAULT_.variant_transcript_consequence_amino_acid_reference, domain=VariantTranscriptConsequence, range=Optional[Union[str, BiologicalSequence]])

slots.variant_transcript_consequence_amino_acid_variant = Slot(uri=DEFAULT_.amino_acid_variant, name="variant transcript consequence_amino acid variant", curie=DEFAULT_.curie('amino_acid_variant'),
                   model_uri=DEFAULT_.variant_transcript_consequence_amino_acid_variant, domain=VariantTranscriptConsequence, range=Optional[Union[str, BiologicalSequence]])

slots.variant_transcript_consequence_codon_reference = Slot(uri=DEFAULT_.codon_reference, name="variant transcript consequence_codon reference", curie=DEFAULT_.curie('codon_reference'),
                   model_uri=DEFAULT_.variant_transcript_consequence_codon_reference, domain=VariantTranscriptConsequence, range=Optional[str])

slots.variant_transcript_consequence_codon_variant = Slot(uri=DEFAULT_.codon_variant, name="variant transcript consequence_codon variant", curie=DEFAULT_.curie('codon_variant'),
                   model_uri=DEFAULT_.variant_transcript_consequence_codon_variant, domain=VariantTranscriptConsequence, range=Optional[str])

slots.variant_transcript_consequence_cdna_start = Slot(uri=DEFAULT_.cdna_start, name="variant transcript consequence_cdna start", curie=DEFAULT_.curie('cdna_start'),
                   model_uri=DEFAULT_.variant_transcript_consequence_cdna_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.variant_transcript_consequence_cnda_end = Slot(uri=DEFAULT_.cnda_end, name="variant transcript consequence_cnda end", curie=DEFAULT_.curie('cnda_end'),
                   model_uri=DEFAULT_.variant_transcript_consequence_cnda_end, domain=VariantTranscriptConsequence, range=Optional[str])

slots.variant_transcript_consequence_cds_start = Slot(uri=DEFAULT_.cds_start, name="variant transcript consequence_cds start", curie=DEFAULT_.curie('cds_start'),
                   model_uri=DEFAULT_.variant_transcript_consequence_cds_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.variant_transcript_consequence_cns_end = Slot(uri=DEFAULT_.cns_end, name="variant transcript consequence_cns end", curie=DEFAULT_.curie('cns_end'),
                   model_uri=DEFAULT_.variant_transcript_consequence_cns_end, domain=VariantTranscriptConsequence, range=Optional[str])

slots.variant_transcript_consequence_protein_start = Slot(uri=DEFAULT_.protein_start, name="variant transcript consequence_protein start", curie=DEFAULT_.curie('protein_start'),
                   model_uri=DEFAULT_.variant_transcript_consequence_protein_start, domain=VariantTranscriptConsequence, range=Optional[int])

slots.variant_transcript_consequence_protein_end = Slot(uri=DEFAULT_.protein_end, name="variant transcript consequence_protein end", curie=DEFAULT_.curie('protein_end'),
                   model_uri=DEFAULT_.variant_transcript_consequence_protein_end, domain=VariantTranscriptConsequence, range=Optional[int])

slots.variant_transcript_consequence_hgvs_protein_nomenclature = Slot(uri=DEFAULT_.hgvs_protein_nomenclature, name="variant transcript consequence_hgvs protein nomenclature", curie=DEFAULT_.curie('hgvs_protein_nomenclature'),
                   model_uri=DEFAULT_.variant_transcript_consequence_hgvs_protein_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])

slots.variant_transcript_consequence_hgvs_coding_nomenclature = Slot(uri=DEFAULT_.hgvs_coding_nomenclature, name="variant transcript consequence_hgvs coding nomenclature", curie=DEFAULT_.curie('hgvs_coding_nomenclature'),
                   model_uri=DEFAULT_.variant_transcript_consequence_hgvs_coding_nomenclature, domain=VariantTranscriptConsequence, range=Optional[str])
