from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Carrier
from .serializers import CarrierSerializer
import pandas as pd
import datetime

class UploadRoutes(APIView):
    def post(self, request):
        file = request.FILES['file']
        df = pd.read_excel(file)
        for _, row in df.iterrows():
            carrier = Carrier(
                origin_postcode=row['Origin Postcode'],
                destination_postcode=row['Destination Postcode'],
                max_capacity=row['Max Capacity (in CC)'],
                available_capacity=row['Available Capacity (in CC)'],
                max_vol_length=row['Max Volumetric Length (cm)'],
                available_vol_length=row['Available Volumetric Length (cm)'],
                max_vol_breadth=row['Max Volumetric Breadth (cm)'],
                available_vol_breadth=row['Available Volumetric Breadth (cm)'],
                max_vol_height=row['Max Volumetric Height (cm)'],
                available_vol_height=row['Available Volumetric Height (cm)'],
                cost_per_cc_km=row['Cost Margin'],
                currency=row['Currency'],
                cost_margin=row['Cost Margin'],
                uom=row['UOM'],
                trip_start_datetime=pd.to_datetime(row['Trip Start Date Time']),
                trip_end_datetime=pd.to_datetime(row['Trip End Date Time']) if pd.notnull(row['Trip End Date Time']) else None,
                carrier_name=row['Carrier Name'],
                cargo_allowable=row['Cargo Allowable'],
                truck_type=row['Truck Type'] if pd.notnull(row['Truck Type']) else None
            )
            carrier.save()
        return Response("Routes uploaded successfully", status=status.HTTP_201_CREATED)