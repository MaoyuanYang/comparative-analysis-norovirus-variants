# README: Evolutionary Analysis of Norovirus GII.4 Sydney Variant

## Project Information

* **Thesis Title**: Comparative analysis of evolutionary patterns of genomes of major norovirus variants
* **Author**: Yang Maoyuan
* **Institution**: Beijing Jiaotong University
* **Date**: June 2023

## Project Overview

This study uses bioinformatics methods to investigate the molecular mechanisms behind the prolonged prevalence of the Norovirus GII.4 Sydney variant since 2012. This breaks the established pattern of GII.4 variants being replaced every 2-5 years.

The research compares the evolutionary differences between the Sydney variant and other major variants, such as Den Haag and New Orleans, focusing on their genomes, the key structural protein VP1, and major antigenic epitopes. The central hypothesis is that the genomic stability and minor antigenic changes of the Sydney variant are the primary reasons for its persistent circulation.

## Key Findings

* **Greater Stability in the VP1 Region**: Compared to other major variants, the GII.4 Sydney variant has fewer Single Nucleotide Polymorphisms (SNPs) in the VP1 coding region, indicating greater stability at the nucleotide level.
* **Limited Impact of Linked Mutations**: While the Sydney variant exhibits a high rate of linked SNP mutations, these linkages rarely affect the crucial VP1 coding region or its main antigenic sites.
* **Minor Changes in Key Antigenic Sites**: The Sydney variant shows significantly fewer amino acid substitutions in the key antigenic epitopes that drive viral evolution (specifically epitopes C and G) and in five critical antigenic sites. This suggests it has faced less selective pressure, and its antigenic properties have changed little.
* **Potential Immune Evasion Mechanism**: The typical mutation bias (C-to-U, U-to-C, A-to-G, G-to-A) is less pronounced in the Sydney variant. This suggests it may be able to inhibit or evade the antiviral effects of the host's RNA-editing enzymes (APOBEC and ADAR).
* **Identification of Potential New Strains**: Phylogenetic analysis identified three strains (KY628449.1, MT221660.2, MW045405.1) with significant antigenic changes that could potentially trigger a new epidemic.

## Methodology

* **Data Source**: Norovirus GII.4 genome sequences were retrieved from the NCBI database.
* **Sequence Processing**: Sequences were aligned using MAFFT. MEGA7 was used for manual adjustments and phylogenetic tree construction.
* **Diversity Analysis**: Custom Python scripts were used to analyze Single Nucleotide Polymorphisms (SNPs), SNP linkage, amino acid sequence diversity, and Shannon entropy.

## Source Code

All Python source code used for the analysis in this study is available at the following repository:
* **Code Repository**: [https://github.com/MaoyuanYang/comparative-analysis-norovirus-variants](https://github.com/MaoyuanYang/comparative-analysis-norovirus-variants)

## How to Cite

If you reference this work in your research, please use the following citation:

Yang, M. (2023). *Comparative analysis of evolutionary patterns of genomes of major norovirus variants* (Bachelor's thesis). Beijing Jiaotong University, Beijing.
