# BirdID — Ethical reflection and data card

**AI for Good · Hackathon 7: Eyes on Earth · SDG 15: Life on Land**

## Short ethical reflection

We reused 502 labelled images from the Roboflow Universe dataset “Bird Species Classification” and trained DINOv3 Small in Roboflow. BirdID is intended to encourage biodiversity learning, not to establish reliable wildlife records. Its reported test results come from only 50 images and do not prove performance on new Dutch photographs. Restricted categories, non-local species, a visible “placeholder” label, blur and unfamiliar birds could cause incorrect or absent predictions; a supplied screenshot already shows an empty result at a 50% threshold. If used for real decisions, mistakes could mislead sightings records or conservation priorities. Users should verify suggestions independently, avoid uploading identifiable people or sensitive nest locations, and never rely on BirdID alone for conservation, animal handling or wildlife-management decisions.

## Data card

### Purpose and intended use

BirdID aims to help students and beginner birdwatchers learn about bird diversity through photograph-based identification suggestions. The intended audience is in The Hague and the Netherlands. This is an educational classification prototype, not a population-counting tool, a verified species survey or a conservation decision system. The SDG 15 connection is biodiversity awareness; no measurable ecological benefit has been established.

### Dataset composition

The supplied version screenshot shows **502 images**, split into **351 training**, **101 validation** and **50 test** images. The project summary reports **eight bird categories**. The per-class screenshot also includes a “placeholder” label; its role and the complete class list must be checked in Roboflow before claiming a clean eight-species taxonomy. Visible labels such as “bald eagle” and “blue jay” show that the category set is not established as a representative list of local Dutch birds. Full per-class training counts and original geographic coverage are unknown.

### Training and evaluation

**Model:** DINOv3 Small, trained in Roboflow. The supplied model page shows training complete and an update on 27 October 2026.

**Reported evaluation:** precision 100%, recall 97.5%, F1 98.6%, at the dashboard’s 17% confidence threshold on 50 test images. These are the platform’s reported aggregates; the averaging method and class-level uncertainty have not been established. Do not reinterpret them as a guarantee that 98.6% of all new Dutch photographs will be classified correctly.

**Independent validation:** no evaluation on newly collected Dutch photographs has been documented. Similar or duplicate images across splits could inflate results; this is a risk to investigate, not a confirmed finding. The displayed threshold was selected using the test-set explorer, so it should not be treated as independently validated deployment tuning. Tune settings on validation data and use a separate, untouched evaluation set.

### Limitations and failure modes

1. **Closed category set:** an unsupported species, non-bird or ambiguous scene could receive a misleading supported label or no prediction. There is no demonstrated reliable unknown-species rejection.
2. **Geographic mismatch:** performance on the reused dataset does not establish useful coverage of birds encountered in The Hague.
3. **Image variation:** distant birds, motion blur, poor lighting, occlusion, juvenile plumage and multiple birds in one photograph may reduce reliability. Classification does not establish detection or counting capability.
4. **Threshold sensitivity:** the supplied model screenshot shows an empty prediction at a 50% threshold. Do not treat this as a successful identification. Roboflow’s recommendation also identifies one missed bald-eagle example at 17%; aggregate scores can hide class-specific errors.
5. **Label quality:** the “placeholder” label and truncated category names require a taxonomy and annotation audit.

### Possible harms and safeguards

- **Misleading wildlife records:** an incorrect suggestion could contaminate citizen-science submissions or bias conservation priorities. Require human confirmation before recording a sighting; do not use predictions alone for ecological decisions.
- **Overconfidence:** a score may look like a reliable probability without being calibrated. Present it as a model score, state the supported categories and make “no prediction” explicit.
- **Privacy and sensitive wildlife locations:** photos may contain people, addresses or location metadata that reveal nests. Crop irrelevant personal details, remove location metadata from shared examples and avoid publishing precise sensitive locations.
- **Wildlife disturbance:** gathering data should not involve approaching nests, baiting birds or entering protected areas. Photograph from a safe distance and follow local access rules.
- **Cloud exposure and credentials:** explain that hosted inference sends images to an external service. Verify provider terms, retention and access controls before deployment; do not promise deletion or zero storage without evidence. Store credentials outside the public repository.

### Responsible next steps

Collect a qualifying Dutch dataset covering the actual intended categories, with at least 300 labelled images as required. If using video, avoid counting adjacent near-identical frames as independent evidence; keep an entire recording or capture session in one split. Verify labels, licences and geographic provenance; remove irrelevant labels. Evaluate new photographs from different sessions and locations, including unfamiliar species and difficult images. Log correct, incorrect and absent predictions per category. Finally, connect the trained model to a tested upload app or script and publish reproducible setup instructions without credentials.

## Evidence and unresolved provenance

This document uses the supplied BirdID summary and five supplied Roboflow screenshots: the model overview, threshold/latency explorer, dataset version, class-performance recommendations and confusion-matrix overview. The dataset version is dated **27 October 2026, 16:34**. A Python/Streamlit setup guide was subsequently supplied, describing Roboflow-hosted inference and Streamlit Community Cloud deployment. 