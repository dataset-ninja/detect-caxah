Dataset **Detect (caxah)** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/l/E/qO/xim4ZdDIwbymzUrrROfjn5dkGYflxsCXz02X7LemItFvXwb5oj6O3MRErPN3Ta5NDA87w7CCnNKgqc8qgZV7D0zKaTlrOGQhuWfLrJCHEu3QEtItM8VMiSsdeu5f.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Detect (caxah)', dst_path='~/dtools/datasets/Detect (caxah).tar')
```
The data in original format can be 🔗[downloaded here](https://universe.roboflow.com/s-o33ou/detect-caxah/dataset/1/download)