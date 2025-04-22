### Headers ###

# Event Number
# Commentary
# Q Curve File
# Q Comment
# TEQ File
# TEQ Comment
# Tune File
# FLower
# FUpper
# Peak Amp (V)
# Peak Center (MHz)
# Beam ON
# RF Level (dBm)
# IF Atten (dB)
# Task3 Temperature
# Task3 Pressure
# NMR Channel
# ADC_1
# ADC_2
# ... (Up to 400)
# ADC_400

def Write_To_CSV(df, Save_Path Commentary, QCurveFile, QComment, TEQFile, TEQComment, TuneFile, 
                 FLower, FUpper, PeakAmp, PeakCenter, BeamON, RFLevel, IFAtten, 
                 Task3Temperature, Task3Pressure, NMRChannel, sigArray):


    import pandas as pd
    import datetime 

    try:

        ### Create Event Number based on current timestamp ###
        EventNumber = int(datetime.datetime.now().timestamp())

        base_data = [EventNumber, Commentary, QCurveFile, QComment, TEQFile, TEQComment, TuneFile, 
                FLower, FUpper, PeakAmp, PeakCenter, BeamON, RFLevel, IFAtten, 
                Task3Temperature, Task3Pressure, NMRChannel]

        base_headers = ["Event Numbers", "Commentary", "Q Curve File", "Q Comment", "TEQ File", "TEQ Comment", "Tune File", 
                "Flower", "FUpper", "Peak Amp (V)", "Peak Center (MHz)", "Beam ON", "RF Level (dBm)", "IF Atten (dB)", 
                "Task3 Temperature", "Task3 Pressure", "NMR Channel"]
        
        signal_headers = [f"ADC_{i+1}" for i in range(len(sigArray))]   
        
        all_headers = base_headers + signal_headers

        data = base_data + sigArray
        
        df = pd.concat([df, new_row], ignore_index=True)
        
        df.to_csv(Save_Path, index=False)

        return 1 ### Return 1 if successful (LabView requires a return value)

    except Exception as e:
        print(f"Error: {e}")
        return e