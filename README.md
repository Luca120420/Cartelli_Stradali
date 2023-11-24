# Traffic Sign Recognition

## Descrizione
Questo progetto contiene due script Python per il riconoscimento e la classificazione di segnali stradali utilizzando modelli di machine learning.

### traffic_sign.py
Lo script `traffic_sign.py` si occupa del training di un modello di classificazione dei segnali stradali utilizzando la libreria Keras e TensorFlow. Il modello viene addestrato su un dataset di immagini di segnali stradali e valutato su un set di test.

### gui.py
Il file `gui.py` implementa un'interfaccia grafica (GUI) per consentire agli utenti di caricare un'immagine contenente un segnale stradale e ottenere la sua classificazione utilizzando il modello addestrato.

## Dipendenze
- numpy
- pandas
- matplotlib
- cv2
- tensorflow
- PIL
- tkinter (per l'interfaccia grafica)
- scikit-learn
- keras

## Istruzioni
1. Assicurati di avere tutte le dipendenze installate.
2. Esegui lo script `traffic_sign.py` per addestrare il modello.
3. Esegui lo script `gui.py` per utilizzare l'interfaccia grafica e classificare le immagini dei segnali stradali.

## Note
- Il modello addestrato viene salvato come `my_model.h5` dopo l'addestramento.
- Assicurati di avere il file `traffic_classifier.h5` (modello addestrato) nella stessa directory di `gui.py` per poterlo utilizzare correttamente.

---