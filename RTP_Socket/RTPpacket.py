
class RTPpacket:

	class RTPHeader:
		'''
		Class RTPHeader
		@parameter  Version: (2 bits) Indicates the version of the protocol. Current version is 2.
		@parameter  P (Padding): (1 bit) Used to indicate if there are extra padding bytes at the end of the RTP packet. 
		@parameter  X (Extension): (1 bit) Indicates presence of an Extension header between standard header and payload data. This is application or profile specific. 
		@parameter  CC (CSRC count): (4 bits) Contains the number of CSRC identifiers (defined below) that follow the fixed header.
		@parameter  M (Marker): (1 bit) Used at the application level and defined by a profile. If it is set, it means that the current data has some special relevance for the application.
		@parameter  PT (Payload type): (7 bits) Indicates the format of the payload and determines its interpretation by the application.
		@parameter  SeqNumber: (16 bits) The sequence number is incremented by one for each RTP data packet sent and is to be used by the receiver to detect packet loss and to restore packet sequence. 
        @parameter  TimeStamp: (32 bits) Used by the receiver to play back the received samples at appropriate time and interval. 
        @parameter  SSRC: (32 bits) Synchronization source identifier uniquely identifies the source of a stream. 
        @parameter  CSRC: (32 bits each, number indicated by CSRC count field) Contributing source IDs enumerate contributing sources to a stream which has been generated from multiple sources.
        @parameter  HeaderExtension: (4*CC bits) The first 32-bit word contains a profile-specific identifier (16 bits) and a length specifier (16 bits) that indicates the length of the extension (EHL = extension header length) in 32-bit units, excluding the 32 bits of the extension header.
		'''
		self.Version = b'00'
		self.P = b'0'
		self.X = b'0'
		self.CC = b'0000'
		self.M = b'0'
		self.PT = b'0000000'
        self.SeqNumber = b'0000000000000000' #16bit
    	self.TimeStamp = b'00000000000000000000000000000000'#32bit
        self.SSRC = b'00000000000000000000000000000000'#32bit
        self.CSRC = b'00000000000000000000000000000000'#32bit
        self.HeaderExtension = 
    
    def getHeader:
      	header = 
        
    def setVersion(version_in):
      	'''
        Set the Version parameter of the RTP Header.
		@parameter  Version: (2 bits) Indicates the version of the protocol. Current version is 2.
    	'''
        self.Version = version_in
    
    def setPadding(p_in):
      	'''
        Set the Padding parameter of the RTP Header.
		@parameter  P (Padding): (1 bit) Used to indicate if there are extra padding bytes at the end of the RTP packet. 
                                A padding might be used to fill up a block of certain size, for example as required by an encryption algorithm. 
                                The last byte of the padding contains the number of padding bytes that were added (including itself).
    	'''
        self.P = p_in
        
    def setExtension(x_in):
      	'''
        Set the Extension parameter of the RTP Header.
		@parameter  X (Extension): (1 bit) Indicates presence of an Extension header between standard header and payload data. 
        							This is application or profile specific. 
    	'''
        self.X = x_in
          
    def setCSRCcount(cc_in):
      	'''
        Set the CSRC count parameter of the RTP Header.
		@parameter  CC (CSRC count): (4 bits) Contains the number of CSRC identifiers (defined below) that follow the fixed header.
    	'''
        self.CC = cc_in
	
    def setMarker(m_in):
      	'''
        Set the Marker parameter of the RTP Header.
		@parameter  M (Marker): (1 bit) Used at the application level and defined by a profile. 
        						If it is set, it means that the current data has some special relevance for the application.
    	'''
        self.M = m_in
    
    '''
    Payload Type Dictionary based on the RFC3551 standard https://tools.ietf.org/html/rfc3551#section-6
    formating is PT : encoding name, media type, clock rate
    
    
    payloadTypeDict = {0: ["PCMU",A,8000],
                       3: ["GSM",A,8000],
                       4: ["G723",A,8000],
                       5: ["DVI4",A,8000],
                       6: ["DVI4",A,16000],
                       7: ["LPC",A,8000],
                       8: ["PCMA",A,8000],
                       9: ["G722",A,8000],
                       10: ["L16",A,44100],
                       11: ["L16",A,44100],
                       12: ["QCELP",A,8000],
                       13: ["CN",A,8000],
                       14: ["MPA",A,90000],
                       15: ["G728",A,8000],
                       16: ["DVI4",A,11025],
                       17: ["DVI4",A,22050],
                       18: ["G729",A,8000],
                       25: ["CelB",V,90000],
                       26: ["JPEG",V,90000],
                       28: ["nv",V,90000],
                       31: ["H261",V,90000],
                       32: ["MPV",V,90000],
                       33: ["MP2T",AV,90000],
                       34: ["H263",V,90000]
                      }
    '''
    
    def setPayloadType(pt_in):
      	'''
        Set the Payload type parameter of the RTP Header.
		@parameter  PT (Payload type): (7 bits) Indicates the format of the payload and determines its interpretation by the application. 
                                      This is specified by an RTP profile. 
                                      For example, see RTP Profile for audio and video conferences with minimal control (RFC 3551).
    	'''
        self.PT = pt_in
            
    def setSequenceNumber(seqnumber_in):
      	'''
        Set the Sequence number parameter of the RTP Header.
		@parameter  Sequence number: (16 bits) The sequence number is incremented by one for each RTP data packet sent and is to be used by 
                                    the receiver to detect packet loss and to restore packet sequence. 
                                    The RTP does not specify any action on packet loss; it is left to the application to take appropriate action. 
                                    For example, video applications may play the last known frame in place of the missing frame.
      	'''
        self.SeqNumber = seqnumber_in
            
    def setTimestamp(timestamp_in):
      	'''
        Set the Timestamp parameter of the RTP Header.
		@parameter  Timestamp: (32 bits) Used by the receiver to play back the received samples at appropriate time and interval. 
                              When several media streams are present, the timestamps may be independent in each stream.
                              For example, an audio application that samples data once every 125 µs (8 kHz, a common sample rate in digital telephony) 
                                would use that value as its clock resolution. Video streams typically use a 90 kHz clock. The clock granularity is one of 
                                the details that is specified in the RTP profile for an application.
      	'''
        self.TimeStamp = timestamp_in
        
    def setSSRC(ssrc_in):
      	'''
        Set the SSRC parameter of the RTP Header.
		@parameter  SSRC: (32 bits) Synchronization source identifier uniquely identifies the source of a stream. 
        				The synchronization sources within the same RTP session will be unique.
      	'''
        self.SSRC = ssrc_in
            
    def setCSRC(csrc_in):
      	'''
        Set the CSRC parameter of the RTP Header.
		@parameter  CSRC: (32 bits each, number indicated by CSRC count field) Contributing source IDs enumerate contributing sources 
        				to a stream which has been generated from multiple sources.
      	'''
        self.CSRC = csrc_in
            
            
    def setHeaderExtension(headerextension_in):
      	'''
        Set the Header extension parameter of the RTP Header.
		@parameter   Header extension: (optional, presence indicated by Extension field) The first 32-bit word contains a profile-specific 
                                      identifier (16 bits) and a length specifier (16 bits) that indicates the length of the extension (EHL = extension header length) 
                                      in 32-bit units, excluding the 32 bits of the extension header.
      	'''
        self.HeaderExtension = headerextension_in
        
           
    def getVersion(version_in):
      	#get the Version parameter of the RTP Header.
		return self.Version
    
    def getPadding(p_in):
      	#get the Padding parameter of the RTP Header.
		return self.P
        
    def getExtension(x_in):
      	#get the Extension parameter of the RTP Header.
		return self.X
          
    def getCSRCcount(cc_in):
      	#get the CSRC count parameter of the RTP Header.
		return self.CC
	
    def getMarker(m_in):
      	#get the Marker parameter of the RTP Header.
		return self.M
    
    def getPayloadType(pt_in):
      	#get the Payload type parameter of the RTP Header.
		return self.PT
            
    def getSequenceNumber(seqnumber_in):
      	#get the Sequence number parameter of the RTP Header.
		return self.SeqNumber
            
    def getTimestamp(timestamp_in):
      	#get the Timestamp parameter of the RTP Header.
		return self.TimeStamp
        
    def getSSRC(ssrc_in):
      	#get the SSRC parameter of the RTP Header.
		return self.SSRC
            
    def getCSRC(csrc_in):
      	#get the CSRC parameter of the RTP Header.
		return self.CSRC
               
    def getHeaderExtension(headerextension_in):
      	#get the Header extension parameter of the RTP Header.
		return self.HeaderExtension
        
    #end RTP Header
    
#end RTP packet
        
        
        
        
        
        
        
        
        
        
        