import cv2
import numpy as np
from PIL import Image
import io

class ROIDetector:
    """
    A class to detect the optic cup in retinal images and assess glaucoma risk.
    
    This implementation is based on the provided notebook and adapted for integration
    with the Khaire Health platform.
    """
    
    def __init__(self):
        self.image = None
        self.processed_image = None
        self.bbox = None
        
    def load_image(self, image):
        """
        Load an image for processing.
        
        Args:
            image: A PIL Image object or path to image file
            
        Returns:
            bool: True if image loaded successfully
        """
        try:
            # If PIL Image is passed, convert to OpenCV format
            if isinstance(image, Image.Image):
                img_array = np.array(image.convert('RGB'))
                # Convert RGB to BGR (OpenCV format)
                self.image = img_array[:, :, ::-1].copy()
            else:
                # Assume it's a file path
                self.image = cv2.imread(str(image))
                
            if self.image is None:
                raise ValueError("Image could not be loaded or converted")
                
            return True
        except Exception as e:
            print(f"Error loading image: {e}")
            return False
    
    def process_image(self):
        """
        Process the image to detect the optic cup and assess glaucoma likelihood.
        
        Returns:
            dict: Detection results including bounding box, cup-to-disc ratio, and glaucoma risk assessment
        """
        if self.image is None:
            return None
            
        # Create a copy for drawing
        image_with_box = self.image.copy()
        
        # Convert to grayscale
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        
        # Apply binary thresholding
        _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
        
        # Apply morphological operations
        kernel = np.ones((10, 10), np.uint8)
        dilated = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, kernel)
        
        # Find contours
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if not contours:
            return {
                "detection_status": "No optic cup detected",
                "glaucoma_risk": "Unknown",
                "confidence": 0,
                "cup_to_disc_ratio": None,
                "bbox": None,
                "processed_image": self.image
            }
            
        # Find largest contour (assumed to be optic cup)
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Get bounding box coordinates
        x, y, w, h = cv2.boundingRect(largest_contour)
        
        # Add padding to bounding box
        padding = 100
        x_pad = max(0, x - padding)
        y_pad = max(0, y - padding)
        w_pad = min(w + (2 * padding), self.image.shape[1] - x_pad)
        h_pad = min(h + (2 * padding), self.image.shape[0] - y_pad)
        
        # Draw rectangle on image
        cv2.rectangle(
            image_with_box,
            (x_pad, y_pad),
            (x_pad + w_pad, y_pad + h_pad),
            (255, 0, 0),
            2
        )
        
        # Calculate cup-to-disc ratio (simplified estimate)
        # In a real implementation, this would use more sophisticated methods
        cup_area = cv2.contourArea(largest_contour)
        # Estimate disc area with padding
        disc_area = (w_pad * h_pad)
        cup_to_disc_ratio = min(cup_area / max(disc_area, 1), 1.0)
        
        # Assess glaucoma risk based on cup-to-disc ratio
        # Note: These thresholds are examples and should be validated in a clinical setting
        if cup_to_disc_ratio > 0.7:
            risk = "High"
            confidence = 85.0 + (cup_to_disc_ratio - 0.7) * 50
        elif cup_to_disc_ratio > 0.5:
            risk = "Moderate"
            confidence = 60.0 + (cup_to_disc_ratio - 0.5) * 125
        else:
            risk = "Low"
            confidence = max(40.0 + cup_to_disc_ratio * 40, 25.0)
            
        self.processed_image = image_with_box
        self.bbox = (x_pad, y_pad, w_pad, h_pad)
        
        return {
            "detection_status": "Optic cup detected",
            "glaucoma_risk": risk,
            "confidence": min(confidence, 99.0),  # Cap confidence at 99%
            "cup_to_disc_ratio": cup_to_disc_ratio,
            "bbox": self.bbox,
            "processed_image": self.cv2_to_pil(image_with_box)
        }
        
    def cv2_to_pil(self, cv_image):
        """Convert OpenCV image to PIL Image"""
        cv_image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        return Image.fromarray(cv_image_rgb)
        
    def get_processed_image(self):
        """Return the processed image with detections"""
        if self.processed_image is not None:
            return self.cv2_to_pil(self.processed_image)
        return None
